import parameters as para
import filter_target_files as ftr
import write_insert as wi
import read_gain as read
import advance_cryptography as adv


def obtain_filter_list():
    files_list = ftr.find_target_files(para.original_directoriy, para.mark_sign_reveal)
    return files_list


def writing_file(files_array):
    for index in files_array:
        content = read.reading_gain(index)

        res_cont = adv.decryption(content, para.secret_key)
        if res_cont != False:
            wi.write_insert_into(
                index,
                para.mark_sign_reveal,
                para.mark_sign_uncover,
                str(res_cont).strip(),
            )


# files_set = obtain_filter_list()
# print(files_set)

# writing_file(files_set)
