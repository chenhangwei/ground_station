import rclpy
from rclpy.node import Node
class GroundStationNode(Node):
    def __init__(self):
        super().__init__('ground_station_node')
        self.get_logger().info('Ground Station Node has been started')
        self.create_timer(1, self.timer_callback)
        self.counter = 0
    def timer_callback(self):
        self.counter += 1
        self.get_logger().info('Counter: %d' % self.counter)
def main(args=None):
    rclpy.init(args=args)
    node = GroundStationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()