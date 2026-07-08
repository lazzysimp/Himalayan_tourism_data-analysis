from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import os


class Tourism:

        # ================= Database Connection =================

    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tourism_management"
        )

        # ================= Test Connection =================

    def test_connection(self):
        try:
            conn = self.connect_db()

            if conn.is_connected():
                messagebox.showinfo("Success", "Database Connected Successfully!")

            conn.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))

        except Exception as e:
            messagebox.showerror("Error", str(e))

        # ================= Add Data =================

    def add_data(self):

        if self.var_customer.get() == "" or self.var_phone.get() == "":
            messagebox.showerror(
                "Error",
                "Customer Name and Phone Number are required"
            )
            return

        try:

            # Calculate Total Amount
            total = float(self.var_price.get()) * int(self.var_travellers.get())
            self.var_total.set(str(total))

            conn = self.connect_db()
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO bookings
            (
            customer_name,
            phone,
            destination,
            state,
            package_type,
            travellers,
            check_in,
            check_out,
            hotel_type,
            room_type,
            package_price,
            total_amount,
            booking_status,
            email,
            booked_by,
            remarks
            )

            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,

            (

            self.var_customer.get(),
            self.var_phone.get(),
            self.var_destination.get(),
            self.var_state.get(),
            self.var_package.get(),
            self.var_travellers.get(),
            self.var_checkin.get(),
            self.var_checkout.get(),
            self.var_hotel.get(),
            self.var_room.get(),
            self.var_price.get(),
            self.var_total.get(),
            self.var_status.get(),
            self.var_email.get(),
            self.var_booked.get(),
            self.txtNotes.get("1.0", END)

            ))

            conn.commit()
            conn.close()
            self.fetch_data()

            messagebox.showinfo("Success", "Booking Added Successfully")

        except Exception as e:
            messagebox.showerror("Error", str(e))


    # ================= Fetch Data =================

    def fetch_data(self):

        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM bookings")

        rows = cursor.fetchall()

        if len(rows) != 0:

            self.booking_table.delete(*self.booking_table.get_children())

            for row in rows:
                self.booking_table.insert("", END, values=row)

        conn.close()
            
        # ================= Destination to State =================

    def destination_state(self, event=""):

        state = self.state_dict.get(self.var_destination.get(), "")

        self.var_state.set(state)

        # ================= Calculate Total Amount =================

    def calculate_total(self, event=""):

        try:

            price = float(self.var_price.get())
            travellers = int(self.var_travellers.get())

            total = price * travellers

            self.var_total.set(total)

        except:

            self.var_total.set("")

        # ================= Constructor =================

    def __init__(self, root):

        self.root = root
        self.root.title("HIMALAYAN TOURS & TRAVEL MANAGEMENT SYSTEM")
        self.root.geometry("1550x800+0+0")
        # ================= Variables =================

        self.var_destination = StringVar()
        self.var_booking = StringVar()
        self.var_customer = StringVar()
        self.var_phone = StringVar()
        self.var_state = StringVar()
        self.var_package = StringVar()
        self.var_travellers = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_hotel = StringVar()
        self.var_room = StringVar()
        self.var_price = StringVar()
        self.var_total = StringVar()
        self.var_occupancy = StringVar()
        self.var_email = StringVar()
        self.var_booked = StringVar()
        self.var_remark = StringVar()
        self.var_status = StringVar()

        # Destination -> State Mapping (Used Later)
        self.state_dict = {
            "Manali": "Himachal Pradesh",
            "Shimla": "Himachal Pradesh",
            "Leh": "Ladakh",
            "Srinagar": "Jammu & Kashmir",
            "Gangtok": "Sikkim",
            "Kasol": "Himachal Pradesh",
            "Auli": "Uttarakhand",
            "Mussoorie": "Uttarakhand",
            "Nainital": "Uttarakhand",
            "Spiti Valley": "Himachal Pradesh",
            "Dharamshala": "Himachal Pradesh",
            "Dalhousie": "Himachal Pradesh",
            "Khajjiar": "Himachal Pradesh",
            "Pahalgam": "Jammu & Kashmir",
            "Gulmarg": "Jammu & Kashmir",
            "Sonamarg": "Jammu & Kashmir",
            "Ranikhet": "Uttarakhand",
            "Almora": "Uttarakhand",
            "Munsiyari": "Uttarakhand",
            "Tawang": "Arunachal Pradesh",
            "Ziro": "Arunachal Pradesh",
            "Kalpa": "Himachal Pradesh",
            "Lachung": "Sikkim",
            "Yumthang": "Sikkim",
            "Pelling": "Sikkim"
        }

        # ================= Title =================

        lbltitle = Label(
            self.root,
            text="HIMALAYAN TOURS & TRAVEL MANAGEMENT SYSTEM",
            bd=15,
            relief=RIDGE,
            fg="#006400",
            bg="white",
            font=("Times New Roman", 32, "bold")
        )
        lbltitle.pack(side=TOP, fill=X)

        # ================= Main Frame =================

        DataFrame = Frame(self.root, bd=15, relief=RIDGE)
        DataFrame.place(x=0, y=80, width=1535, height=400)

        # ================= Left Frame =================

        DataFrameLeft = LabelFrame(
            DataFrame,
            bd=10,
            relief=RIDGE,
            padx=10,
            text="Booking Information",
            font=("Arial", 12, "bold")
        )
        DataFrameLeft.place(x=0, y=5, width=1000, height=350)

        # ================= Right Frame =================

        DataFrameRight = LabelFrame(
            DataFrame,
            bd=10,
            relief=RIDGE,
            padx=10,
            text="Booking Notes",
            font=("Arial", 12, "bold")
        )
        DataFrameRight.place(x=1005, y=5, width=500, height=350)

        # ================= Destination =================

        Label(
            DataFrameLeft,
            text="Destination",
            font=("Arial", 11, "bold")
        ).grid(row=0, column=0, sticky=W, pady=4)

        comboDestination = ttk.Combobox(
            DataFrameLeft,
            textvariable=self.var_destination,
            width=28,
            font=("Arial", 11),
            state="readonly"
        )

        comboDestination["values"] = (
            "Manali",
            "Shimla",
            "Leh",
            "Srinagar",
            "Gangtok",
            "Kasol",
            "Auli",
            "Mussoorie",
            "Nainital",
            "Spiti Valley",
            "Dharamshala",
            "Dalhousie",
            "Khajjiar",
            "Pahalgam",
            "Gulmarg",
            "Sonamarg",
            "Ranikhet",
            "Almora",
            "Munsiyari",
            "Tawang",
            "Ziro",
            "Kalpa",
            "Lachung",
            "Yumthang",
            "Pelling"
        )

        comboDestination.set("Select Destination")
        comboDestination.grid(row=0, column=1, padx=5, pady=4)
        comboDestination.bind("<<ComboboxSelected>>", self.destination_state)

        # ================= Booking Fields =================

        fields = [

            "Customer Name",
            "Phone Number",
            "State",
            "Package Type",
            "No. Of Travelers",
            "Check In Date",
            "Check Out Date",
            "Email",
            "Hotel Type",
            "Room Type",
            "Package Price",
            "Total Amount",
            "Booking Status",
            "Booked By",
            "Remarks"

        ]
        variables = [

            self.var_customer,
            self.var_phone,
            self.var_state,
            self.var_package,
            self.var_travellers,
            self.var_checkin,
            self.var_checkout,
            self.var_email,

            self.var_hotel,
            self.var_room,
            self.var_price,
            self.var_total,
            self.var_status,
            self.var_booked,
            self.var_remark

        ]

        # ================= Left Column =================

        for i in range(7):

            Label(
                DataFrameLeft,
                text=fields[i],
                font=("Arial", 11, "bold")
            ).grid(row=i+1, column=0, sticky=W, pady=4)

            # State should be Read Only
            if fields[i] == "State":

                Entry(
                    DataFrameLeft,
                    textvariable=self.var_state,
                    width=30,
                    font=("Arial", 11),
                    state="readonly"
                ).grid(row=i+1, column=1, padx=5)

            # Package Type Combobox
            elif fields[i] == "Package Type":

                comboPackage = ttk.Combobox(
                    DataFrameLeft,
                    textvariable=self.var_package,
                    width=28,
                    font=("Arial", 11),
                    state="readonly"
                )

                comboPackage["values"] = (
                    "Adventure",
                    "Family",
                    "Luxury"
                )

                comboPackage.grid(row=i+1, column=1, padx=5)

            elif fields[i] == "No. Of Travelers":

                traveller_entry = Entry(
                    DataFrameLeft,
                    textvariable=self.var_travellers,
                    width=30,
                    font=("Arial",11)
                )

                traveller_entry.grid(row=i+1,column=1,padx=5)

                traveller_entry.bind("<KeyRelease>", self.calculate_total)

            else:

                Entry(
                    DataFrameLeft,
                    textvariable=variables[i],
                    width=30,
                    font=("Arial",11)
                ).grid(row=i+1,column=1,padx=5)

        # ================= Right Column =================

        for i in range(7,14):

            Label(
                DataFrameLeft,
                text=fields[i],
                font=("Arial", 11, "bold")
            ).grid(row=i-7, column=2, sticky=W, padx=15, pady=4)

            # Hotel Type Combobox
            if fields[i] == "Hotel Type":

                comboHotel = ttk.Combobox(
                    DataFrameLeft,
                    textvariable=self.var_hotel,
                    width=28,
                    font=("Arial", 11),
                    state="readonly"
                )

                comboHotel["values"] = (
                    "3 Star",
                    "4 Star",
                    "5 Star"
                )

                comboHotel.grid(row=i-7, column=3)

            # Room Type Combobox
            elif fields[i] == "Room Type":

                comboRoom = ttk.Combobox(
                    DataFrameLeft,
                    textvariable=self.var_room,
                    width=28,
                    font=("Arial", 11),
                    state="readonly"
                )

                comboRoom["values"] = (
                    "Single",
                    "Double",
                    "Suite"
                )

                comboRoom.grid(row=i-7, column=3)

            # Booking Status Combobox
            elif fields[i] == "Booking Status":

                comboStatus = ttk.Combobox(
                    DataFrameLeft,
                    textvariable=self.var_status,
                    width=28,
                    font=("Arial",11),
                    state="readonly"
                )

                comboStatus["values"] = (
                    "Pending",
                    "Confirmed",
                    "Completed",
                    "Cancelled"
                )

                comboStatus.grid(row=i-7, column=3)

            # Auto Calculated Fields
            elif fields[i] == "Total Amount":

                Entry(
                    DataFrameLeft,
                    textvariable=variables[i],
                    width=30,
                    font=("Arial", 11),
                    state="readonly"
                ).grid(row=i-7, column=3)

            else:

                Entry(
                    DataFrameLeft,
                    textvariable=variables[i],
                    width=30,
                    font=("Arial", 11)
                ).grid(row=i-7, column=3)

        # ================= Booking Notes =================

        self.txtNotes = Text(
            DataFrameRight,
            font=("Arial", 12),
            width=52,
            height=18
        )

        self.txtNotes.pack(fill=BOTH, expand=True)

        # ================= Button Frame =================

        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE)
        ButtonFrame.place(x=0, y=485, width=1535, height=70)

        btnwidth = 18
         # ================= Button Frame =================

        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE)
        ButtonFrame.place(x=0, y=485, width=1535, height=70)

        btnwidth = 18

        Button(
            ButtonFrame,
            text="Add Booking",
            bg="green",
            fg="white",
            width=btnwidth,
            font=("Arial",11,"bold"),
            command=self.add_data
        ).grid(row=0,column=0)

        Button(
            ButtonFrame,
            text="Show Data",
            bg="#2E8B57",
            fg="white",
            width=btnwidth,
            font=("Arial",11,"bold"),
            command=self.fetch_data
        ).grid(row=0,column=1)

        Button(
            ButtonFrame,
            text="Update",
            bg="#2E8B57",
            fg="white",
            width=btnwidth,
            font=("Arial",11,"bold"),
            command=self.update_data
        ).grid(row=0,column=2)

        Button(
            ButtonFrame,
            text="Delete",
            bg="#B22222",
            fg="white",
            width=btnwidth,
            font=("Arial",11,"bold"),
            command=self.delete_data
        ).grid(row=0,column=3)

        Button(
            ButtonFrame,
            text="Reset",
            bg="#FF8C00",
            fg="white",
            width=btnwidth,
            font=("Arial",11,"bold"),
            command=self.reset_data
        ).grid(row=0,column=4)

        Button(
            ButtonFrame,
            text="Dashboard",
            bg="#1E90FF",
            fg="white",
            width=btnwidth,
            font=("Arial",11,"bold"),
            command=lambda: os.system("python dashboard_analysis.py")
        ).grid(row=0,column=5)

        Button(
            ButtonFrame,
            text="Exit",
            bg="red",
            fg="white",
            width=btnwidth,
            font=("Arial", 11, "bold"),
            command=self.root.destroy
        ).grid(row=0, column=6)

        # ================= Table Frame =================

        DetailsFrame = Frame(self.root, bd=15, relief=RIDGE)
        DetailsFrame.place(x=0, y=560, width=1535, height=210)

        # ================= Search Frame =================

        SearchFrame = LabelFrame(
            DetailsFrame,
            bd=8,
            relief=RIDGE,
            text="Search Booking",
            font=("Arial", 11, "bold")
        )

        SearchFrame.pack(fill=X)

        Label(
            SearchFrame,
            text="Search By",
            font=("Arial", 11, "bold")
        ).grid(row=0, column=0, padx=10, pady=5)

        self.search_by = ttk.Combobox(
            SearchFrame,
            width=18,
            state="readonly",
            font=("Arial", 11)
        )

        self.search_by["values"] = (
            "Customer Name",
            "Destination",
            "Phone Number"
        )

        self.search_by.current(0)
        self.search_by.grid(row=0, column=1, padx=5)

        self.search_txt = Entry(
            SearchFrame,
            width=30,
            font=("Arial", 11)
        )

        self.search_txt.grid(row=0, column=2, padx=5)

        Button(
            SearchFrame,
            text="Search",
            bg="#2E8B57",
            fg="white",
            font=("Arial",10,"bold"),
            width=12,
            command=self.search_data
        ).grid(row=0,column=3,padx=5)

        Button(
            SearchFrame,
            text="Show All",
            bg="#1E90FF",
            fg="white",
            font=("Arial",10,"bold"),
            width=12,
            command=self.fetch_data
        ).grid(row=0,column=4,padx=5)

        # ================= Treeview =================

        TableFrame = Frame(DetailsFrame)
        TableFrame.pack(fill=BOTH, expand=True)

        scroll_x = ttk.Scrollbar(TableFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(TableFrame, orient=VERTICAL)

        self.booking_table = ttk.Treeview(
            TableFrame,
        columns=(
            "booking_id",
            "customer_name",
            "phone",
            "destination",
            "state",
            "package_type",
            "travellers",
            "check_in",
            "check_out",
            "hotel_type",
            "room_type",
            "package_price",
            "total_amount",
            "booking_status",
            "email",
            "booked_by",
            "remarks"
        ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.booking_table.xview)
        scroll_y.config(command=self.booking_table.yview)

        self.booking_table["show"] = "headings"

        headings = {

    "booking_id":"Booking ID",
    "customer_name":"Customer Name",
    "phone":"Phone Number",
    "destination":"Destination",
    "state":"State",
    "package_type":"Package Type",
    "travellers":"Travelers",
    "check_in":"Check In",
    "check_out":"Check Out",
    "hotel_type":"Hotel Type",
    "room_type":"Room Type",
    "package_price":"Package Price",
    "total_amount":"Total Amount",
    "booking_status":"Booking Status",
    "email":"Email",
    "booked_by":"Booked By",

}

        for col, head in headings.items():
            self.booking_table.heading(col, text=head)
            self.booking_table.column(col, width=130, anchor=CENTER)

        self.booking_table.pack(fill=BOTH, expand=1)
        self.booking_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        # ================= Get Cursor =================

    def get_cursor(self, event=""):

        cursor_row = self.booking_table.focus()

        contents = self.booking_table.item(cursor_row)

        row = contents["values"]

        if not row:
            return

        self.var_customer.set(row[1])
        self.var_phone.set(row[2])
        self.var_destination.set(row[3])
        self.var_state.set(row[4])
        self.var_package.set(row[5])
        self.var_travellers.set(row[6])
        self.var_checkin.set(row[7])
        self.var_checkout.set(row[8])
        self.var_hotel.set(row[9])
        self.var_room.set(row[10])
        self.var_price.set(row[11])
        self.var_total.set(row[12])
        self.var_status.set(row[13])
        self.var_email.set(row[14])
        self.var_booked.set(row[15])

        self.txtNotes.delete("1.0", END)
        self.txtNotes.insert(END, row[16])

# ================= Update Booking =================

    def update_data(self):

        if self.var_customer.get() == "":
            messagebox.showerror("Error","Please Select a Booking")
            return

        try:

            conn = self.connect_db()
            cursor = conn.cursor()

            cursor.execute("""
            UPDATE bookings SET

            customer_name=%s,
            phone=%s,
            destination=%s,
            state=%s,
            package_type=%s,
            travellers=%s,
            check_in=%s,
            check_out=%s,
            hotel_type=%s,
            room_type=%s,
            package_price=%s,
            total_amount=%s,
            booking_status=%s,
            email=%s,
            booked_by=%s,
            remarks=%s

            WHERE booking_id=%s

            """,

            (

            self.var_customer.get(),
            self.var_phone.get(),
            self.var_destination.get(),
            self.var_state.get(),
            self.var_package.get(),
            self.var_travellers.get(),
            self.var_checkin.get(),
            self.var_checkout.get(),
            self.var_hotel.get(),
            self.var_room.get(),
            self.var_price.get(),
            self.var_total.get(),
            self.var_status.get(),
            self.var_email.get(),
            self.var_booked.get(),
            self.txtNotes.get("1.0",END),

            self.booking_table.item(
                self.booking_table.focus()
            )["values"][0]

            ))

            conn.commit()

            self.fetch_data()

            conn.close()

            messagebox.showinfo("Success","Booking Updated Successfully")

        except Exception as e:
            messagebox.showerror("Error",str(e))

# ================= Delete Booking =================

    def delete_data(self):

        if self.var_customer.get() == "":
            messagebox.showerror("Error","Please Select a Booking")
            return

        try:

            delete = messagebox.askyesno(
                "Delete",
                "Do you want to delete this booking?"
            )

            if delete:

                conn = self.connect_db()
                cursor = conn.cursor()

                booking_id = self.booking_table.item(
                    self.booking_table.focus()
                )["values"][0]

                cursor.execute(
                    "DELETE FROM bookings WHERE booking_id=%s",
                    (booking_id,)
                )

                conn.commit()
                conn.close()

                self.fetch_data()
                self.reset_data()

                messagebox.showinfo(
                    "Success",
                    "Booking Deleted Successfully"
                )

        except Exception as e:
            messagebox.showerror("Error",str(e))


# ================= Reset =================

    def reset_data(self):

        self.var_destination.set("Select Destination")
        self.var_customer.set("")
        self.var_phone.set("")
        self.var_state.set("")
        self.var_package.set("")
        self.var_travellers.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_hotel.set("")
        self.var_room.set("")
        self.var_price.set("")
        self.var_total.set("")
        self.var_status.set("")
        self.var_email.set("")
        self.var_booked.set("")

        self.txtNotes.delete("1.0", END)
        self.fetch_data()


# ================= Search =================

    def search_data(self):

        conn = self.connect_db()
        cursor = conn.cursor()

        field = self.search_by.get()
        value = self.search_txt.get()

        if field == "Customer Name":
            column = "customer_name"

        elif field == "Destination":
            column = "destination"

        elif field == "Phone Number":
            column = "phone"

        cursor.execute(
            f"SELECT * FROM bookings WHERE {column} LIKE %s",
            ("%" + value + "%",)
        )

        rows = cursor.fetchall()

        self.booking_table.delete(*self.booking_table.get_children())

        for row in rows:
            self.booking_table.insert("", END, values=row)

        conn.close()
# ================= MAIN =================

if __name__ == "__main__":
    root = Tk()
    obj = Tourism(root)
    root.mainloop()
