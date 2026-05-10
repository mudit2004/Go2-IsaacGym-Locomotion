from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class Go2RoughCfg( LeggedRobotCfg ):
    class asset( LeggedRobotCfg.asset ):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/go2/go2.urdf'
        name = "go2"
        foot_name = "foot"
        terminate_after_contacts_on = ['base']
        flip_visual_attachments = True
        self_collisions = 1 

    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.4] 
        default_joint_angles = { 
            'FL_hip_joint': 0.1,   'RL_hip_joint': 0.1,
            'FR_hip_joint': -0.1,  'RR_hip_joint': -0.1,
            'FL_thigh_joint': 0.8, 'RL_thigh_joint': 1.0,
            'FR_thigh_joint': 0.8, 'RR_thigh_joint': 1.0,
            'FL_calf_joint': -1.5, 'RL_calf_joint': -1.5,
            'FR_calf_joint': -1.5, 'RR_calf_joint': -1.5
        }

    class control( LeggedRobotCfg.control ):
        stiffness = {'joint': 20.0} 
        damping = {'joint': 0.5}     
        action_scale = 0.25

class Go2RoughCfgPPO( LeggedRobotCfgPPO ):
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'rough_go2'
