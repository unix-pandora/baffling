import os


def find_target_files(folder_path, contain_string):
    target_filelist = []

    # 遍历文件夹路径下的全部文件（包括子目录中的文件）
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 如果文件名包含字符串: contain_string ，则把它的绝对路径加入到列表
            if contain_string in file:
                file_path = os.path.join(root, file)
                target_filelist.append(file_path)

    return target_filelist
