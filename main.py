import subprocess

def get_open_window_titles():
    script = '''
    tell application "System Events"
        set windowTitles to {}
        set procs to every process
        repeat with p from 1 to count of procs
            set theProc to item p of procs
            set theWindows to every window of theProc
            repeat with w from 1 to count of theWindows
                set theWindow to item w of theWindows
                if exists name of theWindow then
                    set end of windowTitles to name of theWindow as string
                end if
            end repeat
        end repeat
        return windowTitles
    end tell
    '''
    try:
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=True)
        return result.stdout.strip().split(", ")
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# 열려있는 창의 제목 출력
open_window_titles = get_open_window_titles()
print(open_window_titles)
