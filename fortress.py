import branch_shackle as brsh
import field_reduction as fir


def reinforce():
    file_arr = brsh.get_filter_list()
    print(file_arr)
    brsh.ergodic_append(file_arr)


def ablation():
    files_set = fir.obtain_filter_list()
    print(files_set)
    fir.writing_file(files_set)


# reinforce()
ablation()
