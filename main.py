from PySimpleGUI import PySimpleGUI as sg
import back #database file

def signup_window(): #signup function
    sg.theme('dark grey 9')
    layout = [
        [sg.Text("don't have an account?")],
        [sg.Text('       user'), sg.Input(key='USUARIO', size=(20, 1))],
        [sg.Text('password'), sg.Input(key='SENHA', password_char='*', size=(20, 1))],
        [sg.Button('sign up')],
        [sg.Checkbox('i have read and i accept the terms')],
        [sg.Text('already have an account?'), sg.Button('login')]
    ]
    return sg.Window('sign up', layout=layout, element_justification='center', finalize=True)

def login_window(): #login function 
    sg.theme('dark grey 9')
    layout = [
        [sg.Text('user       '), sg.Input(key='USUARIO', size=(20, 1))],
        [sg.Text('password'), sg.Input(key='SENHA', password_char='*', size=(20, 1))],
        [sg.Checkbox('stay logged in')],
        [sg.Button('log in'), sg.Button('exit')]
    ]
    return sg.Window('login', layout=layout, finalize=True)

def postLogin_window(): #post login function
    sg.theme('dark grey 9')
    layout = [
        [sg.Text('              logged in succesfully!')],
        [sg.Button('change password'), sg.Button('continue'), sg.Button('logout')]
    ]
    return sg.Window('logged in', layout=layout, finalize=True)

def changePass(): #change password function(still not changeable)
    sg.theme('dark grey 9')
    layout = [
        [sg.Text('please, type your new password')], 
        [sg.Text('   '), sg.Input(key='newPass', password_char='*', size=(20, 1))],
        [sg.Text('        '), sg.Button('   ok   '), sg.Button('cancel')]
    ]
    return sg.Window('change password', layout=layout, finalize=True)

def finalWindow(): #final window function - needs update
    sg.theme('dark grey 9')
    layout = [
        [sg.Text('      the end')]
    ]
    return sg.Window('end', layout=layout, finalize=True)

def postPass_window(): #password changed function (not changeable yet)
    sg.theme('dark grey 9')
    layout = [
        [sg.Text('    password changed succesfully! (or not)')],
        [sg.Text('              '), sg.Button('continue'), sg.Button('logout')]
    ]
    return sg.Window('password changed', layout=layout, finalize=True)

def dbCode(): #register on database
    USUARIO = values['USUARIO'].capitalize()
    SENHA = values['SENHA'].capitalize()

    if USUARIO != '':
        back.write(USUARIO, SENHA)
        #USUARIO = back.read()
        #SENHA = back.read()

#window opening order
janela0, janela1, janela2, janela3, janela4, janela5 = signup_window(), None, None, None, None, None

#learn how to put them all together!
while True:
        window, event, values = sg.read_all_windows()
        if window == janela0 and event == sg.WIN_CLOSED:
            break
        if window == janela1 and event == sg.WIN_CLOSED:
            break
        if window == janela2 and event == sg.WIN_CLOSED:
            break
        if window == janela3 and event == sg.WIN_CLOSED:
            break
        if window == janela4 and event == sg.WIN_CLOSED:
            break
        if window == janela5 and event == sg.WIN_CLOSED:
            break
        
        #sign up
        if window == janela0 and event == 'sign up':
            dbCode()
            janela1 = login_window()
            janela0.hide()
            print("account send to database")

        if window == janela0 and event == 'login':
            janela1 = login_window()
            janela0.hide()

        #log in
        if window == janela1 and event == 'log in':
            print("logged in")
            janela2=postLogin_window()
            janela1.hide()
            
        if window == janela1 and event == 'exit':
            window.close()

        #logged in
        if window == janela2 and event == 'change password':
            janela3 = changePass()
            janela2.hide()

        if window == janela2 and event == 'continue':
            janela4 = finalWindow()
            janela2.hide()

        if window == janela2 and event == 'logout':
            janela1 = login_window()
            janela2.hide()

        #password change
        if window == janela3 and event == '   ok   ':
            janela5 = postPass_window()
            janela3.hide()

        if window == janela3 and event == 'cancel':
            janela2 = postLogin_window()
            janela3.hide()

        #password changed
        if window == janela5 and event == 'change password':
            janela3 = changePass()
            janela5.hide()

        if window == janela5 and event == 'continue':
            janela4 = finalWindow()
            janela5.hide()

        if window == janela5 and event == 'logout':
            janela1 = login_window()
            janela5.hide()

            

  