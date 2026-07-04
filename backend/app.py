print("=== AI VTuber ===")

while True:
    message = input("你：")

    if message.lower() == "exit":
        print("AI：掰掰！")
        break

    print(f"AI：你剛剛說的是：{message}")