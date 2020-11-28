DEBUG_ON = False
STAGE = None


def set_debug_on():
    global DEBUG_ON
    DEBUG_ON = True


def set_debug_off():
    global DEBUG_ON
    DEBUG_ON = False


def set_stage(stage: str):
    global STAGE
    STAGE = stage


def debug(message: str, force=False):
    if DEBUG_ON or force:
        if STAGE is None:
            print(message)
        else:
            print("{}:    {}".format(STAGE, message))

