from tkinter import *
import csv
import tkinter.messagebox
from PIL import ImageTk,Image

class Display:

    login_window = None
    main_window = None
    add_window = None
    search_window = None
    result_window = None
    delete_window = None
    result_delete_window = None
    
    entry_name = None
    entry_password = None
    entry_type = None
    entry_money = None
    entry_quantity = None
    entry_time = None
    entry_place = None
    entry_pic = None

    entry_item = None

    entry_item_delete = None

    check_type = None
    check_money = None
    check_quantity = None
    check_time = None
    check_place = None
    check_pic = None

    var_1 = None
    var_2 = None
    var_3 = None
    var_4 = None
    var_5 = None
    var_6 = None

    ###in result window, this is for reset label
    reset_label = 0

    label_type = None
    label_money = None
    label_quantity = None
    label_time = None
    label_place = None
    label_pic = None

    label_name_product = None
    label_money_product = None
    label_quantity_product = None
    label_time_product = None
    label_place_product = None
    label_pic_product = None
    
    pic_result = None

    button_return = None
    ###

    ###in result delete window, this is for reset label
    choice_delete = []
    list_box_delete = None
    index_list_box_delete = 0

    label_delete_type = None
    label_delete_money = None
    label_delete_quantity = None
    label_delete_time = None
    label_delete_place = None
    label_delete_pic = None

    label_delete_name_product = None
    label_delete_money_product = None
    label_delete_quantity_product = None
    label_delete_time_product = None
    label_delete_place_product = None
    label_delete_pic_product = None

    button_delete = None

    button_delete_run = None

    reset_label_delete = 0
    ###
    
    #def __init__(self):
    
    def mainWindow(self):
        #create font
        large_font = ('times',15, 'bold')
        #create main_window
        self.main_window = Tk()
        self.main_window.title("Phần mềm quản lý dữ liệu")
        self.main_window.geometry('505x600')
        #display picture
        self.displayImage(self.main_window, "pic_1.png", (500,300), 0, 0, 0, 0)
        #create buttons
        button_search = Button(self.main_window, text="TÌM KIẾM DỮ LIỆU", command=self.searchDataWindow, width=30, height=3)
        button_search.config(font=large_font)
        button_search.grid(row=1, column=0, padx=0, pady=0)
        
        button_add = Button(self.main_window, text="THÊM DỮ LIỆU MỚI", command=self.addDataWindow, width=20, height=3)
        button_add.config(font=large_font)
        button_add.grid(row=2, column=0, padx=0, pady=5)
        
        button_delete = Button(self.main_window, text="XÓA DỮ LIỆU", command=self.deleteDataWindow, width=15, height=3)
        button_delete.config(font=large_font)
        button_delete.grid(row=3, column=0, padx=0, pady=0)
        
        self.main_window.mainloop()

    def loginWindow(self, check_user):
        if check_user == 0:
            self.login_window = Tk()
            self.login_window.title("Đăng nhập")
            self.login_window.geometry('270x100')

            label_name = Label(self.login_window, text="Tên tài khoản:")
            label_password = Label(self.login_window, text="Mật khẩu:")
            self.entry_name = Entry(self.login_window)
            self.entry_password = Entry(self.login_window, show="*")

            label_name.grid(row=0, column=0)
            label_password.grid(row=1, column=0)
            self.entry_name.grid(row=0, column=2)
            self.entry_password.grid(row=1, column=2)

            self.entry_name.insert(0, "hoakiengsadec")
            
            ####need delete
            self.entry_password.insert(0, "1234")
            ####
            
            button_login = Button(self.login_window, text="Đăng nhập", command=self.checkUser).grid(row=2, column=2)
            
            self.login_window.mainloop()

        else:
            self.login_window.destroy()
            self.mainWindow()

    def checkUser(self):
        check = Data()
        if check.user(self.entry_name.get(), self.entry_password.get()) == True:
            self.loginWindow(check_user = 1)
        else:
            self.notificationBox("Thông báo", "Sai mật khẩu hoặc tên tài khoản!")

    def addDataWindow(self):
        #create font
        normal_font = (15)
        #create add_window
        self.main_window.destroy()
        self.add_window = Tk()
        self.add_window.title("Phần mềm quản lý dữ liệu")
        self.add_window.geometry('470x330')

        label_type = Label(self.add_window, text="Nhập tên (VD: Chau Lan)")
        label_type.config(font=normal_font)
        
        label_money = Label(self.add_window, text="Nhập số tiền (VD: 50000)")
        label_money.config(font=normal_font)
        
        label_quantity = Label(self.add_window, text="Nhập số lượng (VD: 50 cai)")
        label_quantity.config(font=normal_font)
        
        label_time = Label(self.add_window, text="Nhập thời gian mua hàng (VD: 1/1/2019)")
        label_time.config(font=normal_font)
        
        label_place = Label(self.add_window, text="Nhập địa diểm mua hàng (VD: Sa Dec)")
        label_place.config(font=normal_font)
        
        label_pic = Label(self.add_window, text="Nhập tên file ảnh (VD: chau.jpg)")
        label_pic.config(font=normal_font)
        
        self.entry_type = Entry(self.add_window, width=25)
        self.entry_money = Entry(self.add_window, width=25)
        self.entry_quantity = Entry(self.add_window, width=25)
        self.entry_time = Entry(self.add_window, width=25)
        self.entry_place = Entry(self.add_window, width=25)
        self.entry_pic = Entry(self.add_window, width=25)

        label_type.grid(row=0, column=0, padx=0, pady=10)
        label_money.grid(row=1, column=0, padx=0, pady=10)
        label_quantity.grid(row=2, column=0, padx=0, pady=10)
        label_time.grid(row=3, column=0, padx=0, pady=10)
        label_place.grid(row=4, column=0, padx=0, pady=10)
        label_pic.grid(row=5, column=0, padx=0, pady=10)
        self.entry_type.grid(row=0, column=2, padx=5, pady=10)
        self.entry_money.grid(row=1, column=2, padx=5, pady=10)
        self.entry_quantity.grid(row=2, column=2, padx=5, pady=10)
        self.entry_time.grid(row=3, column=2, padx=5, pady=10)
        self.entry_place.grid(row=4, column=2, padx=5, pady=10)
        self.entry_pic.grid(row=5, column=2, padx=5, pady=10)

        ###watch this
        self.entry_pic.insert(0, "chau.jpg")

        button_add = Button(self.add_window, text="Thêm", command=self.beforeSaveData)
        button_add.config(font=normal_font)
        button_add.grid(row=6, column=2, padx=0, pady=25)
        
        button_return = Button(self.add_window, text="Trở lại", command=self.AddWindowReturn)
        button_return.config(font=normal_font)
        button_return.grid(row=6, column=0, padx=0, pady=0)
        

    def beforeSaveData(self):
        if(self.entry_type.get() == '' or self.entry_money.get() == '' or self.entry_quantity.get() == '' or self.entry_time.get() == '' or self.entry_place.get() == '' or self.entry_pic.get() == ''):
            self.notificationBox("Thông báo", "Chưa điền hết thông tin!")
        else:
            add = Data()
            add.saveData(self.entry_type.get(), self.entry_money.get(), self.entry_quantity.get(), self.entry_time.get(), self.entry_place.get(), self.entry_pic.get())
            self.notificationBox("Thông báo", "Thêm thành công!")
        
        
    def searchDataWindow(self):
        #create font
        normal_font = (15)
        times_bold = ('times', 15, 'bold')
        #crete search_window
        self.main_window.destroy()
        self.search_window = Tk()
        self.search_window.title("Phần mềm quản lý dữ liệu")
        self.search_window.geometry('650x250')
        #create var
        self.var_1 = IntVar()
        self.var_2 = IntVar()
        self.var_3 = IntVar()
        self.var_4 = IntVar()
        self.var_5 = IntVar()
        self.var_6 = IntVar()
        #create label
        self.check_type = Checkbutton(self.search_window, text="Tìm tên", variable=self.var_1)
        self.check_money = Checkbutton(self.search_window, text="Tìm số tiền", variable=self.var_2)
        self.check_quantity = Checkbutton(self.search_window, text="Tìm số lượng", variable=self.var_3)
        self.check_time = Checkbutton(self.search_window, text="Tìm thời gian", variable=self.var_4)
        self.check_place = Checkbutton(self.search_window, text="Tìm nơi nhập hàng", variable=self.var_5)
        self.check_pic = Checkbutton(self.search_window, text="Tìm tên file ảnh", variable=self.var_6)

        self.check_type.config(font=normal_font)
        self.check_money.config(font=normal_font)
        self.check_quantity.config(font=normal_font)
        self.check_time.config(font=normal_font)
        self.check_place.config(font=normal_font)
        self.check_pic.config(font=normal_font)
        
        self.check_type.grid(row=0, column=0, sticky=W, padx=0, pady=0)
        self.check_money.grid(row=0, column=1, sticky=W, padx=97, pady=0)
        self.check_quantity.grid(row=0, column=2, sticky=W, padx=0, pady=0)
        self.check_time.grid(row=1, column=0, padx=0, pady=3)
        self.check_place.grid(row=1, column=1, padx=0, pady=3)
        self.check_pic.grid(row=1, column=2, padx=0, pady=3)

        label_item = Label(self.search_window, text="Nhập thông tin cần tìm kiếm vào bên dưới")
        label_item.config(font=times_bold)
        self.entry_item = Entry(self.search_window, width=30)

        label_item.grid(row=2, column=1, padx=0, pady=20)
        self.entry_item.grid(row=3, column=1, padx=0, pady=0)
        #create button
        button_return = Button(self.search_window, text="Trở lại", command=self.SearchWindowReturn)
        button_return.config(font=normal_font)
        button_return.grid(row=4, column=0, padx=0, pady=20)
        
        button_search = Button(self.search_window, text="Tìm kiếm", command=self.beforeSearchData)
        button_search.config(font=normal_font)
        button_search.grid(row=4, column=2, padx=20, pady=20)
    

    def beforeSearchData(self):
        if(self.var_1.get() + self.var_2.get() + self.var_3.get() + self.var_4.get() + self.var_5.get() + self.var_6.get() > 1):
            self.notificationBox("Thông báo", "Vui lòng chỉ chọn một ô")
        elif(self.var_1.get() + self.var_2.get() + self.var_3.get() + self.var_4.get() + self.var_5.get() + self.var_6.get() == 0):
            self.notificationBox("Thông báo", "Chọn một ô để tìm kiếm")
        else:
            if(self.entry_item.get() == ''):
                self.notificationBox("Thông báo", "Chưa điền vào ô thông tin cần tìm")
            else:
                search = Data()
                self.resultWindow(search.searchData(self.entry_item.get(), self.var_1.get(), self.var_2.get(), self.var_3.get(), self.var_4.get(), self.var_5.get(), self.var_6.get()))


    def resultWindow(self, results):
        #create resultWindow
        self.search_window.destroy()
        self.result_window = Tk()
        self.result_window.title("Phần mềm quản lý dữ liệu")
        self.result_window.geometry('1300x550')
        #display None
        self.displayImage(self.result_window, "None.png", (250,250), 0, 0, 0, 0)
        #creat list box
        self.listBox(self.result_window, SINGLE, results, 0, 1, 50, 0, 40, 15)
        

    def displayImage(self, window, file_name, size, r, c, px, py):
        img_ = Image.open(file_name)
        img_ = img_.resize(size)
        img_ = ImageTk.PhotoImage(img_)
        pic = Label(window, image=img_)
        pic.image = img_
        pic.grid(row=r, column=c, padx=px, pady=py)


    def listBox(self, window, mode, data, r, c, px, py, w, h):
        list_box = Listbox(window, selectmode=mode, width=w, height=h)
        for i in data:
            list_box.insert(END, i)
        list_box.grid(row=r, column=c, padx=px, pady=py)
        list_box.bind('<<ListboxSelect>>', self.takeInformation)

    def takeInformation(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        choice = w.get(index)
        self.showInformation(choice)

    def showInformation(self, choice):
        #create font
        normal_font = (30)
        times_bold = ('times', 15, 'bold')
        ###reset label
        if self.reset_label == 1:
            
            self.label_type.grid_forget()
            self.label_money.grid_forget()
            self.label_quantity.grid_forget()
            self.label_time.grid_forget()
            self.label_place.grid_forget()
            self.label_pic.grid_forget()
            
            self.label_name_product.grid_forget()
            self.label_money_product.grid_forget()
            self.label_quantity_product.grid_forget()
            self.label_time_product.grid_forget()
            self.label_place_product.grid_forget()
            self.label_pic_product.grid_forget()
        
            self.pic_result.destroy()

            self.button_return.destroy()
                
            self.reset_label = 0

        self.reset_label += 1
        ###
        #create label
        self.label_type = Label(self.result_window, text="Tên:")
        self.label_money = Label(self.result_window, text="Số tiền:")
        self.label_quantity = Label(self.result_window, text="Số lượng:")
        self.label_time = Label(self.result_window, text="Thời gian mua hàng:")
        self.label_place = Label(self.result_window, text="Địa điểm mua hàng:")
        self.label_pic = Label(self.result_window, text="Tên file ảnh:")

        self.label_type.config(font=times_bold)
        self.label_money.config(font=times_bold)
        self.label_quantity.config(font=times_bold)
        self.label_time.config(font=times_bold)
        self.label_place.config(font=times_bold)
        self.label_pic.config(font=times_bold)
        
        self.label_name_product = Label(self.result_window, text=choice[0])
        self.label_money_product = Label(self.result_window, text=choice[1])
        self.label_quantity_product = Label(self.result_window, text=choice[2])
        self.label_time_product = Label(self.result_window, text=choice[3])
        self.label_place_product = Label(self.result_window, text=choice[4])
        self.label_pic_product = Label(self.result_window, text=choice[5])

        self.label_name_product.config(font=normal_font)
        self.label_money_product.config(font=normal_font)
        self.label_quantity_product.config(font=normal_font)
        self.label_time_product.config(font=normal_font)
        self.label_place_product.config(font=normal_font)
        self.label_pic_product.config(font=normal_font)

        self.label_type.grid(row=2, column=0, sticky=W, padx=0, pady=70)
        self.label_money.grid(row=2, column=2, sticky=W, padx=0, pady=0)
        self.label_quantity.grid(row=2, column=4, sticky=W, padx=100, pady=0)
        self.label_time.grid(row=3, column=0, sticky=W, padx=0, pady=0)
        self.label_place.grid(row=3, column=2, sticky=W, padx=0, pady=0)
        self.label_pic.grid(row=3, column=4, sticky=W, padx=100, pady=0)
        
        self.label_name_product.grid(row=2, column=1, sticky=W, padx=0, pady=0)
        self.label_money_product.grid(row=2, column=3, sticky=W, padx=0, pady=0)
        self.label_quantity_product.grid(row=2, column=5, sticky=W, padx=0, pady=0)
        self.label_time_product.grid(row=3, column=1, sticky=W, padx=0, pady=0)
        self.label_place_product.grid(row=3, column=3, sticky=W, padx=0, pady=0)
        self.label_pic_product.grid(row=3, column=5, sticky=W, padx=0, pady=0)
        
        ###display image
        img_result = Image.open(choice[5])
        img_result = img_result.resize((250,250))
        img_result = ImageTk.PhotoImage(img_result)
        self.pic_result = Label(self.result_window, image=img_result)
        self.pic_result.image = img_result
        self.pic_result.grid(row=0, column=0, padx=0, pady=0)
        ###
        self.button_return = Button(self.result_window, text="Trở lại", command=self.ResultWindowReturn)
        self.button_return.config(font=normal_font)
        self.button_return.grid(row=4, column=2, sticky=W, padx=0, pady=50)
            
    def deleteDataWindow(self):
        #show notification
        self.notificationBox("Thông báo", "Một khi đã xóa dữ liệu sẽ mất vĩnh viễn")
        #create delete_window
        self.main_window.destroy()
        self.delete_window = Tk()
        self.delete_window.geometry('510x150')
        #create font
        normal_font = (30)
        times_bold = ('times', 15, 'bold')
        #create label
        label_item_delete = Label(self.delete_window, text="Nhập tên sản phẩm cần xóa vào bên dưới")

        self.entry_item_delete = Entry(self.delete_window, width=35)

        label_item_delete.config(font=times_bold)
        label_item_delete.grid(row=0, column=2, padx=0, pady=0)

        self.entry_item_delete.grid(row=1, column=2, padx=0, pady=10)
        #create button
        button_search = Button(self.result_window, text="Tìm kiếm", command=self.beforeSearchDeleteData)
        button_search.config(font=normal_font)
        button_search.grid(row=3, column=3, padx=0, pady=0)

        button_return = Button(self.result_window, text="Trở lại", command=self.DeleteWindowReturn)
        button_return.config(font=normal_font)
        button_return.grid(row=3, column=0, padx=10, pady=0)

    ###bug
        #def zoomImage(self):
        #self.zoom_window = Tk()
        #self.zoom_window.title("Ảnh phóng to")
        #self.zoom_window.geometry('1000x1000')
    ###

    def beforeSearchDeleteData(self):
        if(self.entry_item_delete.get() == ''):
            self.notificationBox("Thông báo", "Chưa nhập dữ liệu cần xóa")
        else:
            search_2 = Data()
            self.resultDeleteWindow(search_2.searchData(self.entry_item_delete.get(), 1, 0, 0, 0, 0, 0))

    def resultDeleteWindow(self, results):
        #create result delete window
        self.delete_window.destroy()
        self.result_delete_window = Tk()
        self.result_delete_window.geometry('550x600')
        #create list box
        self.list_box_delete = Listbox(self.result_delete_window, selectmode=SINGLE, width=40, height=15)
        for i in results:
            self.list_box_delete.insert(END, i)
        self.list_box_delete.grid(row=0, column=0, padx=0, pady=0)
        self.list_box_delete.bind('<<ListboxSelect>>', self.takeDeleteInformation)

    def takeDeleteInformation(self, event):
        w = event.widget
        self.index_list_box_delete = int(w.curselection()[0])
        self.choice_delete = w.get(self.index_list_box_delete)
        self.showDeleteInformation()
        
    def showDeleteInformation(self):
        #create font
        normal_font = (30)
        times_bold = ('times', 15, 'bold')
        ###reset label
        if self.reset_label_delete == 1:
            
            self.label_delete_type.grid_forget()
            self.label_delete_money.grid_forget()
            self.label_delete_quantity.grid_forget()
            self.label_delete_time.grid_forget()
            self.label_delete_place.grid_forget()
            self.label_delete_pic.grid_forget()
            
            self.label_delete_name_product.grid_forget()
            self.label_delete_money_product.grid_forget()
            self.label_delete_quantity_product.grid_forget()
            self.label_delete_time_product.grid_forget()
            self.label_delete_place_product.grid_forget()
            self.label_delete_pic_product.grid_forget()

            self.button_delete.destroy()
            self.button_delete_return.destroy()
                
            self.reset_label_delete = 0

        self.reset_label_delete += 1
        ###
        #create label
        self.label_delete_type = Label(self.result_delete_window, text="Tên:")
        self.label_delete_money = Label(self.result_delete_window, text="Số tiền:")
        self.label_delete_quantity = Label(self.result_delete_window, text="Số lượng:")
        self.label_delete_time = Label(self.result_delete_window, text="Thời gian mua hàng:")
        self.label_delete_place = Label(self.result_delete_window, text="Địa điểm mua hàng:")
        self.label_delete_pic = Label(self.result_delete_window, text="Tên file ảnh:")

        self.label_delete_type.config(font=times_bold)
        self.label_delete_money.config(font=times_bold)
        self.label_delete_quantity.config(font=times_bold)
        self.label_delete_time.config(font=times_bold)
        self.label_delete_place.config(font=times_bold)
        self.label_delete_pic.config(font=times_bold)

        self.label_delete_name_product = Label(self.result_delete_window, text=self.choice_delete[0])
        self.label_delete_money_product = Label(self.result_delete_window, text=self.choice_delete[1])
        self.label_delete_quantity_product = Label(self.result_delete_window, text=self.choice_delete[2])
        self.label_delete_time_product = Label(self.result_delete_window, text=self.choice_delete[3])
        self.label_delete_place_product = Label(self.result_delete_window, text=self.choice_delete[4])
        self.label_delete_pic_product = Label(self.result_delete_window, text=self.choice_delete[5])

        self.label_delete_name_product.config(font=normal_font)
        self.label_delete_money_product.config(font=normal_font)
        self.label_delete_quantity_product.config(font=normal_font)
        self.label_delete_time_product.config(font=normal_font)
        self.label_delete_place_product.config(font=normal_font)
        self.label_delete_pic_product.config(font=normal_font)

        self.label_delete_type.grid(row=0, column=1, sticky=N, padx=0, pady=0)
        self.label_delete_money.grid(row=1, column=1, sticky=N, padx=0, pady=0)
        self.label_delete_quantity.grid(row=2, column=1, sticky=N, padx=0, pady=30)
        self.label_delete_time.grid(row=3, column=1, sticky=N, padx=0, pady=0)
        self.label_delete_place.grid(row=4, column=1, sticky=N, padx=0, pady=30)
        self.label_delete_pic.grid(row=5, column=1, sticky=N, padx=0, pady=0)
        
        self.label_delete_name_product.grid(row=0, column=2, sticky=N, padx=0, pady=0)
        self.label_delete_money_product.grid(row=1, column=2, sticky=N, padx=0, pady=0)
        self.label_delete_quantity_product.grid(row=2, column=2, sticky=N, padx=0, pady=30)
        self.label_delete_time_product.grid(row=3, column=2, sticky=N, padx=0, pady=0)
        self.label_delete_place_product.grid(row=4, column=2, sticky=N, padx=0, pady=30)
        self.label_delete_pic_product.grid(row=5, column=2, sticky=N, padx=0, pady=0)
        #create button
        self.button_delete = Button(self.result_delete_window, text="Xóa dữ liệu", command=self.deleteItem)
        self.button_delete.config(font=normal_font)
        self.button_delete.grid(row=1, column=0, sticky=N)

        self.button_delete_return = Button(self.result_delete_window, text="Trở về", command=self.ResultDeleteWindow)
        self.button_delete_return.config(font=normal_font)
        self.button_delete_return.grid(row=6, column=1, sticky=W, padx=0, pady=30)

    def deleteItem(self):
        #create loading window
##        loading_window = Tk()
##        loading_window.geometry('100x100')
##        label_loading = Label(loading_window, text="Đang xóa dữ liệu")
##        label_loading.pack()
        #delete item was choosen
        del_item = Data()
        del_item.deleteData(self.choice_delete)
        #delete it in listbox
        self.list_box_delete.delete(self.index_list_box_delete)
##      loading_window.destroy()
        self.notificationBox("Thông báo", "Xóa thành công")

    def AddWindowReturn(self):
        self.add_window.destroy()
        self.mainWindow()

    def SearchWindowReturn(self):
        self.search_window.destroy()
        self.mainWindow()

    def ResultWindowReturn(self):
        self.reset_label = 0
        self.result_window.destroy()
        self.mainWindow()

    def DeleteWindowReturn(self):
        self.delete_window.destroy()
        self.mainWindow()

    def ResultDeleteWindow(self):
        self.reset_label_delete = 0
        self.result_delete_window.destroy()
        self.mainWindow()

    def notificationBox(self, title, message):
        tkinter.messagebox.showinfo(title, message)
        

class Data:

    #def __init__(self, name, password):
        
        
    def user(self, name_input, password_input):
        with open('User.txt','r') as read_file:
            reader = csv.DictReader(read_file)
            for row in reader:
                if (row["name"] == name_input) and (row["password"] == password_input):
                    read_file.close()
                    return True
                else:
                    read_file.close()
                    return False

    #bug: when first time add data, row[0] = row[1]
    def saveData(self, data_1, data_2, data_3, data_4, data_5, data_6):
        with open(r'Data.txt','a',newline='') as write_file:
            f = ['Loai','SoTien','SoLuong','ThoiGian','NoiNhapHang','FileAnh']
            writer = csv.DictWriter(write_file, f)
            writer.writerow({'Loai':data_1,'SoTien':data_2,'SoLuong':data_3,'ThoiGian':data_4,'NoiNhapHang':data_5,'FileAnh':data_6})
            write_file.close()

    def searchData(self, item, check_1, check_2, check_3, check_4, check_5, check_6):
        result = []
        #result = Display()
        with open('Data.txt','r') as read_file:
            reader = csv.DictReader(read_file)
            if(check_1 == 1):
                for row in reader:
                    if(row["Loai"].lower() == item.lower()):
                        result.append([row["Loai"],row["SoTien"],row["SoLuong"],row["ThoiGian"],row["NoiNhapHang"],row["FileAnh"]])
                read_file.close()
                return result
            elif(check_2 == 1):
                for row in reader:
                    if(row["SoTien"] == item):
                        result.append([row["Loai"],row["SoTien"],row["SoLuong"],row["ThoiGian"],row["NoiNhapHang"],row["FileAnh"]])
                read_file.close()
                return result
            elif(check_3 == 1):
                for row in reader:
                    if(row["SoLuong"].lower() == item.lower()):
                        result.append([row["Loai"],row["SoTien"],row["SoLuong"],row["ThoiGian"],row["NoiNhapHang"],row["FileAnh"]])
                read_file.close()
                return result
            elif(check_4 == 1):
                for row in reader:
                    if(row["ThoiGian"] == item):
                        result.append([row["Loai"],row["SoTien"],row["SoLuong"],row["ThoiGian"],row["NoiNhapHang"],row["FileAnh"]])
                read_file.close()
                return result
            elif(check_5 == 1):
                for row in reader:
                    if(row["NoiNhapHang"].lower() == item.lower()):
                        result.append([row["Loai"],row["SoTien"],row["SoLuong"],row["ThoiGian"],row["NoiNhapHang"],row["FileAnh"]])
                read_file.close()
                return result
            elif(check_6 == 1):
                for row in reader:
                    if(row["FileAnh"] == item):
                        result.append([row["Loai"],row["SoTien"],row["SoLuong"],row["ThoiGian"],row["NoiNhapHang"],row["FileAnh"]])
                read_file.close()
                return result

    def writeFirstRow(self):
        with open('Data.txt','w') as write_file:
            writer = csv.writer(write_file)
            writer.writerow(["Loai","SoTien","SoLuong","ThoiGian","NoiNhapHang","FileAnh"])
            write_file.close()

    def deleteData(self, line_delete):
        with open('Data.txt','r') as read_file:
            flag = 0
            reader = csv.DictReader(read_file)
            for row in reader:
                if flag == 0:
                    self.writeFirstRow()
                    if(row["Loai"]!=line_delete[0] or row["SoTien"]!=line_delete[1] or row["SoLuong"]!=line_delete[2] or row["ThoiGian"]!=line_delete[3] or row["NoiNhapHang"]!=line_delete[4] or row["FileAnh"]!=line_delete[5]):
                        self.saveData(row["Loai"],row["SoTien"],row["SoLuong"],row["ThoiGian"],row["NoiNhapHang"],row["FileAnh"])
                else:
                    if(row["Loai"]!=line_delete[0] or row["SoTien"]!=line_delete[1] or row["SoLuong"]!=line_delete[2] or row["ThoiGian"]!=line_delete[3] or row["NoiNhapHang"]!=line_delete[4] or row["FileAnh"]!=line_delete[5]):
                        self.saveData(row["Loai"],row["SoTien"],row["SoLuong"],row["ThoiGian"],row["NoiNhapHang"],row["FileAnh"])
                flag = 1
            read_file.close()

def run():
    show_display = Display()
    show_display.loginWindow(check_user = 0)

if __name__ == "__main__":
    run()
