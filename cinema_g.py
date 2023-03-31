
#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalID
from actionlib import SimpleActionClient
import sys, select, termios, tty
from geometry_msgs.msg import Twist



msg = """
cinema guide robot
-------------------

1 ~ 6 gate


   
CTRL-C to quit
"""


def A_pose():
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.pose.position.x = 1.06239032745
    goal.target_pose.pose.position.y = 3.04575514793
    goal.target_pose.pose.position.z = 0.0
    goal.target_pose.pose.orientation.w = 0.00818751644446
    client.send_goal(goal)
    # client.wait_for_result()
    return goal


def B_pose():
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.pose.position.x = 3.28035974503
    goal.target_pose.pose.position.y = 2.99271726608
    goal.target_pose.pose.position.z = 0.0
    goal.target_pose.pose.orientation.w = 0.7058625101
    client.send_goal(goal)
    # client.wait_for_result()
    return goal

def C_pose():
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.pose.position.x = 6.09785795212
    goal.target_pose.pose.position.y = 2.77076864243
    goal.target_pose.pose.position.z = 0.0
    goal.target_pose.pose.orientation.w = 0.708202912554
    client.send_goal(goal)
    # client.wait_for_result()
    return goal

def D_pose():
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.pose.position.x = 4.80511617661
    goal.target_pose.pose.position.y = 0.862050294876
    goal.target_pose.pose.position.z = 0.0
    goal.target_pose.pose.orientation.w = -0.00749993842815
    client.send_goal(goal)
    # client.wait_for_result()
    return goal

def E_pose():
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.pose.position.x = 4.42496776581
    goal.target_pose.pose.position.y = -1.05161762238
    goal.target_pose.pose.position.z = 0.0
    goal.target_pose.pose.orientation.w = 0.00865122414064
    client.send_goal(goal)
    # client.wait_for_result()
    return goal

def F_pose():
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.pose.position.x = 1.82540941238
    goal.target_pose.pose.position.y = -1.12251734734
    goal.target_pose.pose.position.z = 0.0
    goal.target_pose.pose.orientation.w = 0.00818751644446
    client.send_goal(goal)
    # client.wait_for_result()
    return goal


def Base_pose():
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.pose.position.x = -9.24
    goal.target_pose.pose.position.y = 0.56
    goal.target_pose.pose.position.z = 0.0
    goal.target_pose.pose.orientation.w = 1.0
    client.send_goal(goal)
    # client.wait_for_result()
    return goal


def stopbot():
    cancel_pub = rospy.Publisher('/move_base/cancel', GoalID, queue_size=10)
    goal_id = GoalID()
    goal_id.id
    cancel_pub.publish(goal_id)
   

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key




if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('simple_navigation_goals')

    client = SimpleActionClient('move_base', MoveBaseAction)
    # rospy.loginfo("Waiting for move_base action server...")
    client.wait_for_server()

    # rospy.loginfo("Move base action server found.")
 

    try:
        print (msg)
        
        while True:
            key = getKey()
            if key == '1':
                A_pose()
            elif key == '2':
                B_pose()
            elif key == '3':
                C_pose()
            elif key == '4':
                D_pose()
            elif key == '5':
                E_pose()
            elif key == '6':
                F_pose()
            elif key == '7':
                Base_pose()
            elif key == 's':
                stopbot()
            elif key == '\x03':
                break
    except Exception as e:
        print (e)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        twist = Twist()





    # try:
    #     goal = MoveBaseGoal()
    #     while True:
    #         key =int (getKey())
    #         print(key)
    #         goal.target_pose.header.frame_id = "map"
    #         goal.target_pose.pose.position.x = positions[key][0]
    #         goal.target_pose.pose.position.y = positions[key][1]
    #         goal.target_pose.pose.position.z = positions[key][2]
    #         goal.target_pose.pose.orientation.w = positions[key][3]
    #         client.send_goal(goal)

    #         if key == '9':
    #             stopbot()

    #         elif key == '\x03':
    #             break
        
    # except Exception as e:
    #     print (e)

    # finally:
    #     termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    #     twist = Twist()



    