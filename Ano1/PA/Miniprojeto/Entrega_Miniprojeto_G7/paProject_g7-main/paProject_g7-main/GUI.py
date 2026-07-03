import json, monitor_services
from monitor_services import MonitorService as monitor
from PIL import Image
import cv2
from flask import Flask
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from tkinter import ttk
import Database

main_window = tk.Tk()
main_window.title("Host Monitoring Service")
main_window.geometry("1000x1000")


def search_bar(ip):

    timestamps, results = monitor.get_history(m,ip)

    plt.xticks(timestamps)
    plt.yticks([0,1], ["Offline", "Online"])    

    plt.plot(timestamps, results, marker="x")

    plt.xlabel("Timestamp")
    plt.ylabel("Result")

    plt.show()

def show_hosts(m, table):

    '''
    Juntou-se a search_bar() e show_hosts() numa só
    '''

    # Limpar a tabela
    for row in table.get_children():
        table.delete(row)

    results = m.tests


    hosts_name = []
    hosts_ip = []
    hosts_timestamp_tests = []
    hosts_results_tests = []

    for tc in results:
        
        # Verifica se o ip introduzido na search bar é igual ao ip do objeto em iteração
        # Em caso afirmativo, adiciona á lista de nome e ip
        # Se a search bar estiver vazia adiciona todos
        hosts_name.append(tc.host.name)
        hosts_ip.append(tc.host.ip)

        if tc.test_metrics:

            last_timestamp = tc.test_metrics[-1].timestamp
            last_ping = tc.test_metrics[-1].on

            hosts_timestamp_tests.append(last_timestamp)

            if last_ping:
                hosts_results_tests.append("Online")
            else:
                hosts_results_tests.append("Offline")
        else:
            hosts_timestamp_tests.append("Unknown")
            hosts_results_tests.append("Unknown")

    for i in range(len(hosts_ip)):
        table.insert(parent='',index = i, values=(hosts_name[i], hosts_ip[i], hosts_timestamp_tests[i], hosts_results_tests[i]), tags=('evenrow',))

    table.pack(expand=True, fill=tk.BOTH)



#Export (2 types)
def export_GUI():
    
    pop_up = tk.Toplevel(main_window)
    pop_up.title("Export")
    pop_up.geometry("300x150")
    

    export_data_all_button = tk.Button(pop_up, text="Export All hosts", command=lambda : GUI_export_data_all(pop_up))
    export_data_single_button = tk.Button(pop_up, text="Export single host", command=lambda : GUI_call_export_data_single(pop_up))


    export_data_all_button.pack()
    export_data_single_button.pack()


def GUI_export_data_all(window):

    window.destroy()
    # All: entry com o destino para onde se vai fazer o export e 
    # um botão OK e ele cria o export, chamando o export_data_all   
    pop_up = tk.Toplevel()
    pop_up.title("Export")
    pop_up.geometry("300x150")

    export_destination_label = tk.Label(pop_up, text="Export Destination file path :")
    export_destination_entry = tk.Entry(pop_up, bg="grey", fg="black")

    export_destination_button = tk.Button(pop_up, text="OK", command=lambda : call_export_data_all_GUI(export_destination_entry.get(), pop_up))


    export_destination_label.pack(pady=10)
    export_destination_entry.pack(pady=10)
    export_destination_button.pack()

def call_export_data_all_GUI(file_path, window):

    if file_path == "":
        tk.messagebox.showinfo("Error", "Need file path")
        return

    result = monitor.export_data_all(file_path)

    if result:
        window.destroy()
    else:
        tk.messagebox.showinfo("Error", "Invalid file path")



def GUI_call_export_data_single(window):
    
    window.destroy()
    # All: entry com o destino para onde se vai fazer o export e 
    # um botão OK e ele cria o export, chamando o export_data_all   
    pop_up = tk.Toplevel()
    pop_up.title("Export")
    pop_up.geometry("300x150")

    ip_destination_label = tk.Label(pop_up, text="Host IP:")
    ip_destination_entry = tk.Entry(pop_up, bg="grey", fg="black")
    export_destination_label = tk.Label(pop_up, text="Export Destination file path :")
    export_destination_entry = tk.Entry(pop_up, bg="grey", fg="black")


    export_destination_button = tk.Button(pop_up, text="OK", command=lambda : call_export_data_single_GUI(export_destination_entry.get(), ip_destination_entry.get(), pop_up))

    ip_destination_label.pack()
    ip_destination_entry.pack()
    export_destination_label.pack(pady=10)
    export_destination_entry.pack(pady=10)
    export_destination_button.pack()
    # Single: duas entries, uma para o IP
    # descobrir qual é que é o objeto com esse IP, e dar à função
    # export_data_single esse objeto (self.hosts)

    # verificar a entry: se tiver vazia, adiciona todos ao export,
    # se não estiver vazio, ele vai procurar pelo host com aquele IP

def call_export_data_single_GUI(file_path, ip, window):

    if not monitor.validate_ip(ip):
        tk.messagebox.showinfo("Error", "Invalid IP address")

    ip_list = []
    host_list = []

    for host in m.hosts:
        ip_list.append(host.ip)
        host_list.append(host)

    

    if ip not in ip_list:
        tk.messagebox.showinfo("Error", "Host not exist")
        return 
        
    if file_path == "":
        tk.messagebox.showinfo("Error", "Need file path")
        return

    result = monitor.export_data_single(host_list[0], file_path)

    if result:
        window.destroy()
    else:
        tk.messagebox.showinfo("Error", "Invalid file path")
            

    



# add hosts Buttons

def add_Host_GUI():
    add_host_file()

def add_host_file():
    
    pop_up = tk.Toplevel(main_window)
    pop_up.title("Add Host")
    pop_up.geometry("300x150")

    path_label = tk.Label(pop_up, text="Hosts File Path:")
    path_entry = tk.Entry(pop_up, bg="grey", fg="black")
    confirm_button = tk.Button(pop_up, text="Confirm", command=lambda : call_to_read_json(path_entry.get(), pop_up))
    qrcode_button = tk.Button(pop_up, text="Use QR Code", command=add_host_QRCode)

    path_label.pack()
    path_entry.pack()
    confirm_button.pack(pady=10)
    qrcode_button.pack(pady=10)

def call_to_read_json( json_file, window):
    # Verifica se foi introduzido algo na entry
    if json_file == "":
        tk.messagebox.showinfo("Error", "File path is required")
        return

    host_dict = monitor.read_json_host(json_file)


    if isinstance(host_dict, str):
        tk.messagebox.showinfo("Error", host_dict)


    host_id = host_dict.get("id")
    ip = host_dict.get("ip")
    name = host_dict.get("name")
    permission_level = host_dict.get("permission_level")

    # Validações obrigatórias para hosts

    for host in m.hosts:

        if host_id == host.id:
            tk.messagebox.showinfo("Error", "Host already exists")
            return
    
    if not host_id or not name:
        tk.messagebox.showinfo("Error", "Missing required fields (id, name).")
        return

    if not ip or not monitor.validate_ip(ip):
        tk.messagebox.showinfo("Error", "Invalid or missing IP address.")
        return

    if not permission_level or not monitor.validate_permission_level(permission_level):
        tk.messagebox.showinfo("Error", "Invalid or missing permission level.")
        return

    # Envio seguro sem depender de índices de listas
    
    data_to_send = []
      
    if "id" in host_dict:
        data_to_send.append(host_dict["id"])
    
    if "ip" in host_dict:
        if monitor.validate_ip(host_dict["ip"]):
            data_to_send.append(host_dict["ip"])

    if "name" in host_dict:
        data_to_send.append(host_dict["name"])

    if "permission_level" in host_dict:
        if monitor.validate_permission_level(host_dict["permission_level"]):
            data_to_send.append(host_dict["permission_level"])

    monitor.add_host(m,data_to_send[0],data_to_send[1],data_to_send[2],data_to_send[3])

    window.destroy()

    
#EXTRA
def add_host_QRCode():

    detector = cv2.QRCodeDetector()
    cam = cv2.VideoCapture(0)

    # Verificar se a webcam abriu
    if not cam.isOpened():
        tk.messagebox.showerror("Webcam Error",
                                "Webcam not available")
        return

    while True:
        ret, frame = cam.read()
        
        if not ret or frame is None:
            print("Empty frame Error —> webcam not available to use in this machine or Failed to grab frame.")
            break

        cv2.imshow("QR Reader", frame)

        data, bbox, _ = detector.detectAndDecode(frame)

        
        if data:
            # abrir pop-up c/ labels, e button que chama o add_host do MonitorService
            data = data.split(';')

            #validar argumentos para o add_host do monitor_services:
            if (int(data[0]) > 0) and ( monitor.validate_ip(data[1]) ) and ( monitor.validate_permission_level(int(data[3])) ):
                
                #novo Pop-Up com campos do data como Labels:
                QR_pop_up = tk.Toplevel(main_window)
                QR_pop_up.title("Read QR Code")
                QR_pop_up.geometry("300x150")

                QR_label1 = tk.Label(QR_pop_up, text=f"Host ID: {data[0]}").pack()
                QR_label2 = tk.Label(QR_pop_up, text=f"Host IP: {data[1]}").pack()
                QR_label3 = tk.Label(QR_pop_up, text=f"Host Name: {data[2]}").pack()
                QR_label4 = tk.Label(QR_pop_up, text=f"Host Permission Level: {data[3]}").pack()               

                #Botão que chama o add_host do MonitorService
                confirm_QRCode_button = tk.Button(QR_pop_up, text="OK", command=lambda: monitor.add_host(m, id=data[0], ip=data[1], name=data[2], permission_level=int(data[3])))
                confirm_QRCode_button.pack(pady=5)
                tk.messagebox.showinfo("Host added with success!")

            else:
                tk.messagebox.showerror("Error occurred while reading the Host QR Code.\n" \
                "Please insert the text fields in the QR Code in this format: id;ip;name;permission_level" \
                "\n(id is a positive integer ;ip is a string with a valid IPv4 address; name is a string; permission_level is an integer between 1 and 5)").pack()

        if cv2.waitKey(1) == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()


# Remove Host:
def remove_host_GUI():

    pop_up = tk.Toplevel(main_window)
    pop_up.title("Remove Host")
    pop_up.geometry("300x300")

    remove_host_label = tk.Label(pop_up, text="IP:")
    remove_host_entry = tk.Entry(pop_up, bg="grey", fg="black")
    remove_host_button = tk.Button(pop_up, text="Confirm", command=lambda: call_remove_host(remove_host_entry.get(), pop_up))
 
    remove_host_label.pack()
    remove_host_entry.pack()
    remove_host_button.pack()
    

def call_remove_host(ip, window):

    # Verifica se foi introduzido algo na entry
    if ip == "":
        tk.messagebox.showinfo("Error", "Please add an IP address.").pack()
        return

    global m
    hosts_to_send = []

    for host in m.hosts:
        if ip == host.ip:
            hosts_to_send.append(host)


    if monitor.validate_ip(ip):
        host_removed = m.remove_host(hosts_to_send)
        
    if host_removed:
        # se flag true, correu bem
        tk.messagebox.showinfo("Host removed with success!")
    else:
        # se flag falsa, retorna um erro e abre pop-up
        tk.messagebox.showinfo("Error removing host.")
    
    window.destroy()
        

def add_Admin_GUI():

    pop_up = tk.Toplevel(main_window)
    pop_up.title("Add Admin")
    pop_up.geometry("300x300")
    
    name_label = tk.Label(pop_up, text="Name:")
    name_entry = tk.Entry(pop_up, bg="grey", fg="black")
    email_label = tk.Label(pop_up, text="Email:")
    email_entry = tk.Entry(pop_up, bg="grey", fg="black")
    password_label = tk.Label(pop_up, text="Password:")
    password_entry = tk.Entry(pop_up, bg="grey", fg="black")
    smtp_server_label = tk.Label(pop_up, text="SMTP:")
    smtp_server_entry = tk.Entry(pop_up, bg="grey", fg="black")
    permission_level_label = tk.Label(pop_up, text="Permission Level:")
    permission_level_entry = tk.Entry(pop_up, bg="grey", fg="black")

    name_label.pack()
    name_entry.pack()
    email_label.pack()
    email_entry.pack()
    password_label.pack()
    password_entry.pack()
    smtp_server_label.pack()
    smtp_server_entry.pack()
    permission_level_label.pack()
    permission_level_entry.pack()
    # criar outra frame com 4 LabelEntries 
    # e outro Botão p/ confirmar (que chama a função )
    # add_admin do monitor_services
    tk.Button(pop_up, text="Confirm", command=lambda: monitor.add_admin(m,name_entry.get(), email_entry.get(), password_entry.get(), smtp_server_entry.get(), int(permission_level_entry.get()))).pack(padx=10)
    tk.messagebox.showinfo("Admin added successfully!")

# Remove Admin:
def remove_Admin_GUI():

    pop_up = tk.Toplevel(main_window)
    pop_up.title("Remove Admin")
    pop_up.geometry("300x300") 

    remove_admin_label = tk.Label(pop_up, text="Email:")
    remove_admin_entry = tk.Entry(pop_up, bg="grey", fg="black")
    remove_admin_button = tk.Button(pop_up, text="Confirm", command=lambda: call_remove_admin(remove_admin_entry.get(), pop_up))
 
    remove_admin_label.pack()
    remove_admin_entry.pack()
    remove_admin_button.pack()
    

def call_remove_admin(email, window):

    global m

    if email == "":
        tk.messagebox.showinfo("Error", "Please write an email address.")
        return

    if email.count('@') == 1:
        admin_removed = monitor.remove_admin(m, email)
        
    if admin_removed:
        # se flag true, correu bem
        tk.messagebox.showinfo("Admin removed with success!")
    else:
        # se flag falsa, retorna um erro e abre pop-up
        tk.messagebox.showinfo("Error removing Admin.")

    window.destroy()

def loop_collect_metrics(m,table):
    m.collect_metrics()
    m.update_Tests_Table()
    show_hosts(m, table,)
    print("Updated Metrics and Database")
    main_window.after(4000, loop_collect_metrics, m,table)


if __name__ == "__main__":

    
    # Search Bar:
    frame_search_bar = tk.Frame(main_window)
    frame_search_bar.pack(fill="x", padx=10, pady=8)
    tk.Label(frame_search_bar, text="Search by IP").pack(side="left")
    search_entry = tk.Entry(frame_search_bar, width=100)
    search_entry.pack(side="left", padx=4)
    tk.Button(frame_search_bar, text="Ok", command=lambda : search_bar(search_entry.get())).pack(side="left", padx=2)



    # zona para as duas frames (gŕafico e Lista de hosts):
    frame_hosts = tk.Frame(main_window,bg="#d9d9d9",highlightbackground="black", highlightthickness=1)

    # Criar Tabela
    table = ttk.Treeview(frame_hosts)

    table["columns"] = ("Name", "IP Address", "Last Ping Timestamp", "Last Ping Result")

    table.column('#0', width=0, stretch=tk.NO)
    table.column('Name', anchor=tk.CENTER, width=200)
    table.column('IP Address', anchor=tk.CENTER, width=200)
    table.column('Last Ping Timestamp', anchor=tk.CENTER, width=200)
    table.column('Last Ping Result', anchor=tk.CENTER, width=200)

    table.heading('#0', text='', anchor=tk.CENTER)
    table.heading('Name', text='Name', anchor=tk.CENTER)
    table.heading('IP Address', text='IP Address', anchor=tk.CENTER)
    table.heading('Last Ping Timestamp', text='Last Ping Timestamp', anchor=tk.CENTER)
    table.heading('Last Ping Result', text='Last Ping Result', anchor=tk.CENTER)

    table.tag_configure('oddrow', background='#E8E8E8')
    table.tag_configure('evenrow', background='#FFFFFF')


    frame_hosts.pack(fill="both", expand=True, padx=20, pady=20)


    # Barra de botões inferiores:
    frame_Buttons = tk.Frame(main_window)
    frame_Buttons.pack(side="bottom", fill="x", padx=10, pady=8)


    tk.Button(frame_Buttons, text="Export", command=export_GUI).pack(side="left", padx=4)
    tk.Button(frame_Buttons, text="Remove Admin", command=remove_Admin_GUI).pack(side="right", padx=4)
    tk.Button(frame_Buttons, text=" Add Admin", command=add_Admin_GUI).pack(side="right", padx=4)
    tk.Button(frame_Buttons, text="Remove Host", command=remove_host_GUI).pack(side="right", padx=4)
    tk.Button(frame_Buttons, text="Add Host", command=add_Host_GUI).pack(side="right", padx=4)


    m = monitor()

    loop_collect_metrics(m,table)

    monitor.innit_list_hosts(m)
    

    main_window.mainloop() 

    Database.engine.dispose()
    