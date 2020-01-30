#include <cdd/setoper.h>
#include <cdd/cdd.h>

#include <stdio.h>
#include <stdlib.h>

double* A_eq_cash = NULL;
double* b_eq_cash = NULL;
double* A_ineq_cash = NULL;
double* b_ineq_cash = NULL;
double* V_cash = NULL;
double* R_cash = NULL;

int cddlib_initialize (void){
  dd_set_global_constants();  /* First, this must be called to use cddlib. */
  return 0;
}

int cddlib_finalize (void){
  dd_free_global_constants();  /* At the end, this must be called. */
  return 0;
}

/*
  A_eq   x + b_eq    = 0
  A_ineq x + b_ineq >= 0
 */
int cddlib_H_to_V (double* A_eq, double* b_eq, double* A_ineq, double* b_ineq, int d, int m_eq, int m_ineq, int* out_n, int* out_s, int verbose)
{
  free(V_cash);
  V_cash = NULL;
  free(R_cash);
  R_cash = NULL;

  dd_PolyhedraPtr poly;
  dd_MatrixPtr A, G;
  dd_ErrorType err;

  A=dd_CreateMatrix(m_eq + m_ineq,d+1);
  for (size_t i = 0; i < m_eq; i++){
    set_addelem(A->linset,i+1);
    dd_set_d(A->matrix[i][0],b_eq[i]);
    for (size_t j = 0; j < d; j++){
      dd_set_d(A->matrix[i][j+1],A_eq[i*d+j]);
    }
  }
  for (size_t i = 0; i < m_ineq; i++){
    dd_set_d(A->matrix[m_eq+i][0],b_ineq[i]);
    for (size_t j = 0; j < d; j++){
      dd_set_d(A->matrix[m_eq+i][j+1],A_ineq[i*d+j]);
    }
  }
  A->representation=dd_Inequality;
  poly=dd_DDMatrix2Poly(A, &err);  /* compute the second (generator) representation */
  if (err==dd_NoError){
    G=dd_CopyGenerators(poly);
    if (verbose){
      printf("\nInput is H-representation:\n");
      dd_WriteMatrix(stdout,A);  printf("\n");
      dd_WriteMatrix(stdout,G);
    }
    int n = 0;
    int s = 0;
    for (size_t i = 0; i < G->rowsize; i++){
      if (dd_get_d(G->matrix[i][0]) ==0) s++;
      else n++;
    }
    *out_n = n;
    *out_s = s;
    int _n = 0;
    int _s = 0;
    V_cash = (double*)malloc(sizeof(double)*n*d);
    R_cash = (double*)malloc(sizeof(double)*s*d);
    for (size_t i = 0; i < G->rowsize; i++){
      if (dd_get_d(G->matrix[i][0])==0){
        for (size_t j = 0; j < d; j++){
          R_cash[s*j+_s] = dd_get_d(G->matrix[i][1+j]);
        }
        _s++;
      }else{
        for (size_t j = 0; j < d; j++){
          V_cash[n*j+_n] = dd_get_d(G->matrix[i][1+j]);
        }
        _n++;
      }
    }

    dd_FreeMatrix(A);
    dd_FreeMatrix(G);
    dd_FreePolyhedra(poly);
    return 0;
  }else{
    dd_WriteErrorMessages(stdout,err);
  }
  return -1;
}

int cddlib_get_V (double* V, double* R, int d, int n, int s)
{
  for(size_t i=0; i < d*n; i++){
    V[i] = V_cash[i];
  }
  for(size_t i=0; i < d*s; i++){
    R[i] = R_cash[i];
  }
  return 0;
}

int cddlib_V_to_H (double* V, double* R, int d, int n, int s, int* out_m_eq, int* out_m_ineq, int verbose)
{
  free(A_eq_cash);
  A_eq_cash = NULL;
  free(b_eq_cash);
  b_eq_cash = NULL;
  free(A_ineq_cash);
  A_ineq_cash = NULL;
  free(b_ineq_cash);
  b_ineq_cash = NULL;

  dd_PolyhedraPtr poly;
  dd_MatrixPtr A, G;
  dd_ErrorType err;

  G=dd_CreateMatrix(n+s,d+1);
  for (size_t i = 0; i < n; i++){
    dd_set_d(G->matrix[i][0],1);
    for (size_t j = 0; j < d; j++){
      dd_set_d(G->matrix[i][j+1],V[j*n+i]);
    }
  }
  for (size_t i = 0; i < s; i++){
    dd_set_d(G->matrix[n+i][0],0);
    for (size_t j = 0; j < d; j++){
      dd_set_d(G->matrix[n+i][j+1],R[j*s+i]);
    }
  }
  G->representation=dd_Generator;
  poly=dd_DDMatrix2Poly(G, &err);  /* compute the second (generator) representation */
  if (err==dd_NoError){
    A=dd_CopyInequalities(poly);
    if (verbose){
      printf("\nInput is V-representation:\n");
      dd_WriteMatrix(stdout,G);  printf("\n");
      dd_WriteMatrix(stdout,A);
    }
    int m_eq = 0;
    int m_ineq = 0;
    for (size_t i = 0; i < A->rowsize; i++){
      if (set_member(i+1,A->linset)) m_eq++;
      else m_ineq++;
    }
    *out_m_eq = m_eq;
    *out_m_ineq = m_ineq;
    int _m_eq = 0;
    int _m_ineq = 0;
    A_eq_cash = (double*)malloc(sizeof(double)*m_eq*d);
    b_eq_cash = (double*)malloc(sizeof(double)*m_eq);
    A_ineq_cash = (double*)malloc(sizeof(double)*m_ineq*d);
    b_ineq_cash = (double*)malloc(sizeof(double)*m_ineq);
    for (size_t i = 0; i < A->rowsize; i++){
      if (set_member(i+1,A->linset)){
        for (size_t j = 0; j < d; j++){
          A_eq_cash[d*_m_eq+j] = dd_get_d(A->matrix[i][1+j]);
        }
        b_eq_cash[_m_eq] = dd_get_d(A->matrix[i][0]);
        _m_eq++;
      }else{
        for (size_t j = 0; j < d; j++){
          A_ineq_cash[d*_m_ineq+j] = dd_get_d(A->matrix[i][1+j]);
        }
        b_ineq_cash[_m_ineq] = dd_get_d(A->matrix[i][0]);
        _m_ineq++;
      }
    }

    dd_FreeMatrix(A);
    dd_FreeMatrix(G);
    dd_FreePolyhedra(poly);
    return 0;
  }else{
    dd_WriteErrorMessages(stdout,err);
  }
  return -1;
}

int cddlib_get_H (double* A_eq, double* b_eq, double* A_ineq, double* b_ineq, int d , int m_eq, int m_ineq)
{
  for(size_t i=0; i < d*m_eq; i++){
    A_eq[i] = A_eq_cash[i];
  }
  for(size_t i=0; i < m_eq; i++){
    b_eq[i] = b_eq_cash[i];
  }
  for(size_t i=0; i < d*m_ineq; i++){
    A_ineq[i] = A_ineq_cash[i];
  }
  for(size_t i=0; i < m_ineq; i++){
    b_ineq[i] = b_ineq_cash[i];
  }
  return 0;
}
