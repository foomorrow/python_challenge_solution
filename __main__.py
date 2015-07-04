import traceback
total_level = 33
def get_resolve_module(ind):
    try:
        return __import__("c"+str(ind))
    except ImportError as e:
        pass
    except Exception as e:
        print traceback.format_exc()
        print e
        return None

def show_answers():
    resolve_modules = filter(lambda i: i != None and hasattr(i,'answer'), [get_resolve_module(i) for i in range(total_level)])
    print map(lambda i : i.answer,resolve_modules)


if __name__ == '__main__':
    show_answers()
