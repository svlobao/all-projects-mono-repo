import pybullet
import pybullet_data
import time

pybullet.connect(pybullet.GUI)
pybullet.resetSimulation()
pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
pybullet.setGravity(0, 0, -9.80665)
pybullet.setRealTimeSimulation(0)


# Load assets

pybullet.loadURDF("plane.urdf", [0, 0, 0], [0, 0, 0, 1])
targid = pybullet.loadURDF(
    "assets/franka_panda/panda.urdf",
    [0, 0, 0],
    [0, 0, 0, 1],
    useFixedBase=True,
)
obj_of_focus = targid

for step in range(300):
    focus_position, _ = pybullet.getBasePositionAndOrientation(targid)
    pybullet.resetDebugVisualizerCamera(
        cameraDistance=3,
        cameraYaw=0,
        cameraPitch=-40,
        cameraTargetPosition=focus_position,
    )
    pybullet.stepSimulation()
    time.sleep(1)
