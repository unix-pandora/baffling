import getopt
import sys
import branch_shackle as brsh
import field_reduction as fir


def reinforce():
    file_arr = brsh.get_filter_list()
    brsh.ergodic_append(file_arr)


def ablation():
    files_set = fir.obtain_filter_list()
    fir.writing_file(files_set)


def main(argv):
    pattern = ""

    try:
        opts, args = getopt.getopt(
            argv,
            "hu:p:",
            [
                "help",
                "pattern=",
            ],
        )
    except getopt.GetoptError:
        print("error: fortress.py -p <pattern>")
        print("or: fortress.py --pattern=<pattern>")
        print("Option order: 0(reinforce) or 1(ablation)")
        sys.exit(2)

    # 打印 返回值args列表，即其中的元素是那些不含'-'或'--'的参数。
    for i in range(0, len(args)):
        print("Parameter: %s is：%s" % (i + 1, args[i]))

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("command format: fortress.py -p <pattern>")
            print("or: fortress.py --pattern=<pattern>")
            print("Option order: 0(reinforce) or 1(ablation)")
            sys.exit()
        elif opt in ("-p", "--pattern"):
            pattern = arg
    print("pattern: ", pattern)

    if pattern == "0":
        reinforce()
    elif pattern == "1":
        ablation()
    else:
        print("Invaild except option order[ 0(reinforce) or 1(ablation) ]")


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名
    main(sys.argv[1:])
