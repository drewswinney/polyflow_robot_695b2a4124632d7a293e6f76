import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    parameters = json.loads('{"joint":"695b2bb924632d7a293e6f98","control_mode":"position","transport":"can","units":"radians","gear_ratio":1,"smoothing_alpha":0,"can.node_id":0,"can.interface":"socketcan","can.channel":"can0","can.bitrate":1000000,"can.poll_hz":50,"can.request_iq":false,"can.heartbeat_timeout_s":2,"can.enable_closed_loop_on_start":true,"can.torque_constant":0,"limit.lower_position":0,"limit.upper_position":360,"limit.position_step":null,"limit.max_effort":0,"limit.effort_step":0.1,"limit.max_velocity":0,"limit.velocity_step":0.1}')
    configuration = json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')
    inbound_connections = json.loads('[]')
    outbound_connections = json.loads('[]')
    env = {
        "POLYFLOW_NODE_ID": "695b2bd224632d7a293e6fa5",
        "POLYFLOW_PARAMETERS": json.dumps(parameters),
        "POLYFLOW_CONFIGURATION": json.dumps(configuration),
        "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(inbound_connections),
        "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(outbound_connections),
    }

    return LaunchDescription([
        Node(
            package="odrive_s1",
            executable="odrive_s1_node",
            name="odrive_s1_node",
            output="screen",
            additional_env=env
        )
    ])