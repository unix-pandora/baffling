def write_to_new_file(input_filename, sign_name, textcont):
    # 按照点号拆分文件名
    namelist = input_filename.split(".")
    if len(namelist) != 2:
        print(f"Invalid filename format for {input_filename}")
        return

    # 拼接新的文件名前缀和扩展名
    new_prefix = namelist[0] + sign_name
    new_extension = namelist[1]
    newfilename = new_prefix + "." + new_extension

    # 追加写入到新文件
    try:
        with open(newfilename, "a") as file:
            file.write(textcont)
    except Exception as e:
        print(f"Error writing to file {newfilename}: {e}")
