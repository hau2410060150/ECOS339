from StudentManager import StudentManager

qlsv = StudentManager()

while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("********************MENU********************")
    print("**  1. Them sinh vien.                    **")
    print("**  2. Cap nhat thong tin sinh vien by ID.**")
    print("**  3. Xoa sinh vien by ID.               **")
    print("**  4. Tim kiem sinh vien theo ten.       **")
    print("**  5. Sap xep sinh vien theo diem TB.    **")
    print("**  6. Sap xep sinh vien theo ten.        **")
    print("**  7. Hien thi danh sach sinh vien.      **")
    print("**  0. Thoat                              **")
    print("********************************************")

    try:
        key = int(input("Nhap tuy chon: "))
    except ValueError:
        print("\nVui long nhap so!")
        continue

    if key == 1:
        print("\n1. Them sinh vien.")
        qlsv.input_student()
        print("\nThem sinh vien thanh cong!")

    elif key == 2:
        if qlsv.get_student_count() > 0:
            print("\n2. Cap nhat thong tin sinh vien.")
            ID = int(input("Nhap ID: "))
            qlsv.update_student(ID)
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 3:
        if qlsv.get_student_count() > 0:
            print("\n3. Xoa sinh vien.")
            ID = int(input("Nhap ID: "))
            if qlsv.delete_by_id(ID):
                print("\nSinh vien co id =", ID, "da bi xoa.")
            else:
                print("\nSinh vien co id =", ID, "khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 4:
        if qlsv.get_student_count() > 0:
            print("\n4. Tim kiem sinh vien theo ten.")
            name = input("Nhap ten de tim kiem: ")
            search_result = qlsv.find_by_name(name)
            qlsv.show_students(search_result)
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 5:
        if qlsv.get_student_count() > 0:
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sort_by_gpa()
            qlsv.show_students(qlsv.get_student_list())
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 6:
        if qlsv.get_student_count() > 0:
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sort_by_name()
            qlsv.show_students(qlsv.get_student_list())
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 7:
        if qlsv.get_student_count() > 0:
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.show_students(qlsv.get_student_list())
        else:
            print("\nDanh sach sinh vien trong!")

    elif key == 0:
        print("\nBan da chon thoat chuong trinh!")
        break

    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")