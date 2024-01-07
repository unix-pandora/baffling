def write_insert_into(input_filename, prev_sign, new_sign, textcont):
    newfilename = str(input_filename).replace(prev_sign, new_sign)

    # 追加写入到新文件
    try:
        with open(newfilename, "a") as file:
            file.write(textcont)
    except Exception as e:
        print(f"Error writing to file {newfilename}: {e}")
