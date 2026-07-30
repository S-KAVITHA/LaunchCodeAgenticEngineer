# Quality Rubric

## 1. Dimensions

### 1.1 Build Result Accuracy

Measures whether the agent correctly identified the final outcome of the Docker build. A high score requires the stated result (success or failure) to match the actual exit status of the build command.

### 1.2 Error Diagnosis Accuracy

Measures whether the agent correctly identifies the root cause of Docker build failures. A high score requires accurate interpretation of error messages, identification of relevant configuration issues, and avoidance of unrelated troubleshooting steps.

### 1.3 Troubleshooting Guidance Quality

Measures whether the agent provides actionable and appropriate steps to resolve Docker build issues. A high score requires clear commands, logical troubleshooting order, and explanations that help the user understand the fix.

### 1.4 Technical Completeness

Measures whether the agent considers important technical details required for the task. This includes checking Docker configuration, dependencies, environment setup, permissions, networking, and build context when relevant.

### 1.5 Communication Clarity

Measures whether the agent communicates findings and recommendations clearly. A high score requires concise explanations, structured responses, and commands that are easy for users to follow.

### 1.6 Safety and Reliability

Measures whether the agent avoids harmful recommendations and handles sensitive information appropriately. A high score requires avoiding exposure of secrets, warning about credential leaks, and recommending safe operational practices.

