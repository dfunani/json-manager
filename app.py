from sys import argv
from logging import basicConfig, error, info, INFO
from models.base import DevCMS, ResponseType

def main(flags):
    try:
        for flag in flags:
            match flag:
                case "-c":
                    DevCMS.updateCollections("category")
                case "-C":
                    DevCMS.updateCollections("countries")
                case "-l":
                    DevCMS.updateCollections("languages")
                case "-a":
                    DevCMS.updateCollections("category")
                    DevCMS.updateCollections("countries")
                    DevCMS.updateCollections("languages")
        return ResponseType.success
    except BaseException as e:
        error(">>>>>>>>>>>>>>>>>>>>>>>> " + str(e))
        return ResponseType.error


if __name__ == "__main__":
    basicConfig(
        filename="app.log",
        filemode="a",
        format="%(name)s - %(levelname)s - %(message)s",
        level=INFO,
    )
    info("======================== JSON Manager Started =============================")
    if len(argv) <= 1:
        argv.append("-a")
    if main(argv[1:]) == ResponseType.error:
        error(">>>>>>>>>>>>>>>>>>>>>>>> JSON Manager Encountered Issues")
    else:
        info(">>>>>>>>>>>>>>>>>>>>>>>> JSON Manager Stopped")
    info("===========================================================================")
