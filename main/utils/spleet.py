from spleeter.separator import Separator

def spleet(file, stem_count):
    stem = f"spleeter:{stem_count}stems"
    separator = Separator(stem)
    #separator.separate_to_file()
