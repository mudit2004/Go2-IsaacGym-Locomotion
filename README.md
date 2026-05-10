# Massively Parallel PPO Locomotion for Unitree Go2

**Author:** Mudit Golchha | Binghamton University 
**Course:** Intelligent Mobile Robotics 

## Project Overview
This repository contains the custom environment configurations, task registries, and final converged PPO policies for training a Unitree Go2 quadruped in NVIDIA's Isaac Gym. 

By migrating from CPU-bound simulators to a GPU-accelerated tensor pipeline, the policy achieved over **20,000 simulation steps per second**, reaching total gait convergence (999.83 mean episode length) in under two hours on an RTX 4050.

### 🎥 [Watch the Final Trained Policy Video Here](INSERT_YOUR_GOOGLE_DRIVE_LINK_HERE)

## Repository Structure
* `src/envs/go2/go2_config.py`: The Markov Decision Process setup, including the 48-dim observation space, PD controller gains, and the dense semantic reward curriculum.
* `src/envs/__init__.py`: The modified initialization file utilizing a Factory Design Pattern to resolve circular module dependencies.
* `src/utils/task_registry.py`: The decoupled task registration pipeline.
* `checkpoints/final_policy.pt`: The fully converged neural network weights (Iteration 1500).
* `report/`: Contains the formal IEEE conference paper and telemetry graphs.

## Engineering Highlights
1. **Asset Pipeline Migration:** Surgically parsed ROS `package://` URDF paths to allow Isaac Gym to render the visual and collision meshes natively.
2. **Domain Randomization:** Implemented aggressive Sim-to-Real parameter randomization to ensure physical robustness.
3. **Disturbance Rejection:** The final policy exhibits zero steady-state error on planar velocity tracking and flawless recovery from 0.4m initialization drops.
