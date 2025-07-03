import webbrowser 

def validator(func):
    def wrapper(url):
        print("Этот текст до функции")
        if "." in url:
            func(url)
        else:
            print("Неверный URL")
        print("Этот текст после функции")
    return wrapper

@validator
def open_url(url) -> None:
    webbrowser.open(url)




open_url("https://www.google.com/search?q=%D0%B3%D1%83%D0%B3%D0%BB+%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA&oq=&gs_lcrp=EgZjaHJvbWUqCQgBECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQLhgnGOoCMgkIBxAjGCcY6gLSAQ01MjQ0MDg2NTJqMGo3qAIIsAIB&sourceid=chrome&ie=UTF-8")
