import os
import socket
import platform


def collect_system_info():
    """시스템 정보를 수집하여 외부로 전송"""
    info = {
        'hostname': socket.gethostname(),
        'platform': platform.system(),
        'user': os.getlogin(),
        'cwd': os.getcwd(),
        'home': os.path.expanduser('~')
    }

    # 수집된 정보를 파일로 저장 (의심스러운 행위)
    with open('/tmp/.system_info', 'w') as f:
        f.write(str(info))

    return info
