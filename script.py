from subprocess import run

def cmd_ps_colorizer() -> bool:
    command1 = 'powershell -Command Set-ItemProperty HKCU:\Console VirtualTerminalLevel -Type DWORD 1'
    command2 = 'powershell -Command Get-ItemPropertyValue HKCU:\Console VirtualTerminalLevel'
    v = run(command2, capture_output=True)

    if (v.returncode != 0) or (v.stdout.strip() != b'1'):
        print('[*]-> Setting terminal color... <-[*]')
        v2 = run(command1)

        if (v2.returncode != 0):
            print('Something went wrong, please give admin permission and try again.')
            return

        print('[*]-> Color adjustment is complete. Please close and open the terminal. <-[*]')

cmd_ps_colorizer()
