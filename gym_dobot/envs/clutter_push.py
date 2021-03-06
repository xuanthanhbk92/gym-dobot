from gym import utils
from gym_dobot.envs import clutter_env


class DobotClutterPushEnv(clutter_env.DobotClutterEnv, utils.EzPickle):
    def __init__(self, reward_type='sparse',clutter_num=20,rand_dom=False,unity_remote=False):
        initial_qpos = {
            'dobot:slide0': 0.8,
            'dobot:slide1': 1.2,
            'dobot:slide2': -0.04,
            'object0:joint': [1.25, 0.53, 0.032,  1., 0., 0., 0.],
        }
        clutter_env.DobotClutterEnv.__init__(
            self, 'dobot/clutter_push.xml', has_object=True, block_gripper=True, n_substeps=20,
            gripper_extra_height=0.0, target_in_the_air=False, target_offset=0.0,
            obj_range=0.185, target_range=0.2, distance_threshold=0.05,
            initial_qpos=initial_qpos, reward_type=reward_type,
            clutter_num=clutter_num,rand_dom=rand_dom,unity_remote=unity_remote)
        utils.EzPickle.__init__(self)
