import parameters as para
import files_filter as fter
import write_newfile as wri
import read_gain
import advance_cryptography as adv


def get_filter_list():
    files_list = fter.find_files(para.original_directoriy, para.files_types)
    return files_list


def ergodic_append(filename_list):
    for row in filename_list:
        content = read_gain.reading_gain(row)

        result_cont = adv.encryption(content, para.secret_key)
        if result_cont != False:
            wri.write_to_new_file(row, para.mark_sign_reveal, str(result_cont).strip())


# file_arr = get_filter_list()
# print(file_arr)
# ergodic_append(file_arr)
