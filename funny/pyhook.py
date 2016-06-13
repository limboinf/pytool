# coding=utf-8
"""
代码提交前实现自动语法和PEP8检测
    :copyright: (c) 2016 by fangpeng(@beginman.cn).
    :license: MIT, see LICENSE for more details.
"""
import os
import sys
import subprocess


def syntax_checker():
    """
        pyflakes 与 pep8 进行语法与代码风格检查。
        有严重语法错误时提交会被直接拒绝；
        如果有风格问题，会询问提交人员是否继续进行提交
    """
    errors = ''
    warning = ''
    pep8_info = ''

    # 获取有改动的文档
    staged_cmd = 'git diff --staged --name-only HEAD'
    proc = subprocess.Popen(staged_cmd, shell=True, stdout=subprocess.PIPE)
    with proc.stdout as std_out:
        for staged_file in std_out.readlines():
            staged_file = staged_file.strip()

            if not is_python_file(staged_file):
                continue

            stdout, stderr = process('pyflakes %s' % staged_file)
            warning += stdout
            errors += stderr

            stdout, _ = process('flake8 --max-complexity 12 %s' % staged_file)
            pep8_info += stdout

    failed = False
    if is_error(errors) or is_warning(warning) or is_warning(pep8_info):
        failed = True

    return failed


def is_python_file(filename):
    if filename.endswith('.py') and os.path.exists(filename):
        return True

    return False


def process(cmd):
    """ 执行命令, 返回标准输出与错误信息 """
    proc = subprocess.Popen(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    return proc.communicate()


def is_error(errors):
    """ 严重错误，如语法错误等 """
    failed = False
    if errors:
        failed = True
        print ("[failed] You cann't commit, repair the errors "
               "or run `pyflakes` view details:\n"
               "------------------------------")
        print (errors)
    return failed


def is_warning(warning):
    """ 代码规范建议信息 """
    failed = False

    if warning:
        print (warning)
        print ("Encounter some non-standard syntax! "
               "Do you want to correct them? y(es) or n(o):")

        # 从终端输入
        sys.stdin = open('/dev/tty')
        while True:
            input_row = sys.stdin.readline().strip().lower()
            if input_row in ('y', 'yes'):
                failed = True
                break
            elif input_row in ('n', 'no'):
                failed = False
                break
            print('Input y(es) or n(o):')

    return failed


print ('=================== syntax check start =======================')
failed = syntax_checker()
if not failed:
    print (":) All Is OK!")

print ('=================== syntax check end =========================')
sys.exit(1 if failed else 0)
