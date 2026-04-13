# GitHub Actions CI/CD Pipeline

**Name:** Bhanu Reddy  
**Registration Number:** 2022bcd0026  
**Status:** Ready for final testing - Both scenarios

## Project Overview

This project implements a GitHub Actions CI/CD workflow that conditionally deploys a Docker image based on model performance (MSE).

## Workflow Logic

1. **Train Model**: Trains a machine learning model and calculates MSE
2. **Compare Performance**: Compares new MSE with BEST_MSE variable
3. **Conditional Deployment**: 
   - If MSE improves → Build and push Docker image
   - If MSE doesn't improve → Skip deployment

## Author

**Bhanu Reddy**  
Registration Number: 2022bcd0026
