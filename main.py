
if __name__ == '__main__':
    
    from utils import init_log_record
    from utils.args import Args
    from utils.input_interpreter import InputInterperter

    args = Args.parseArgs()

    init_log_record(args.log_level, args.log_file_extension, args.verbose)

    interpreter = InputInterperter()

    interpreter.coord_to_tuple('Z5')