def reading_gain(input_filename):
    try:
        # 读取文件内容
        with open(input_filename, "r") as file:
            textcont = file.read()
            return textcont
    except Exception as e:
        print(f"Error reading file {input_filename}: {e}")
        return
