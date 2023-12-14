import serial
import time

# 打开串口通信
def open_serial(serial_port):
    return serial.Serial(serial_port, 115200)

# 串口测试模式
def serial_test(serial_port):
    ser = open_serial(serial_port)

    while True:
        try:
            user_input = input("请输入要发送的ASCII码 (按q返回主菜单): ")
            if user_input == "q":
                break

            user_input_with_newline = user_input + "\n"
            ser.write(user_input_with_newline.encode())

            received_data = ser.read(ser.in_waiting).decode()
            if received_data:
                print(f"串口响应: {received_data.strip()}")

        except KeyboardInterrupt:
            break

    ser.close()
    print("串口通信已关闭")

# 时钟模式
def clock_mode(serial_port):
    ser = open_serial(serial_port)

    while True:
        try:
            current_time = time.strftime("%H:%M:%S", time.localtime())
            ser.write(current_time.encode() + b'\n')  # 添加回车符
            time.sleep(1)

        except KeyboardInterrupt:
            break

    ser.close()

# 计时器模式（按毫秒计时）
def timer_mode(serial_port):
    ser = open_serial(serial_port)

    start_time = time.time()
    while True:
        try:
            elapsed_time_ms = int((time.time() - start_time) )
            timer_msg = f"Time:{elapsed_time_ms} s"
            ser.write(timer_msg.encode() + b'\n')  # 添加回车符
            time.sleep(1)  # 1秒更新一次
        except KeyboardInterrupt:
            break

    ser.close()

# 主菜单
def main_menu():
    serial_port = input("请输入串口设备 (例如：COM18): ")

    while True:
        print("主菜单:")
        print("1. 串口测试")
        print("2. 时钟模式")
        print("3. 计时器模式")
        print("q. 退出")

        choice = input("请选择操作模式: ")

        if choice == "1":
            serial_test(serial_port)
        elif choice == "2":
            clock_mode(serial_port)
        elif choice == "3":
            timer_mode(serial_port)
        elif choice == "q":
            break
        else:
            print("无效的选项，请重新选择。")

if __name__ == "__main__":
    main_menu()
