import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Đọc dữ liệu từ tệp CSV
raw_data = pd.read_csv("data.csv")

# Xử lý dữ liệu
# Chọn các cột để thực hiện one-hot encoding
cot_one_hot = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
data = pd.get_dummies(raw_data, columns=cot_one_hot)
# Chuẩn hóa dữ liệu
standardScaler = StandardScaler()
cot_chuan_hoa = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
data[cot_chuan_hoa] = standardScaler.fit_transform(data[cot_chuan_hoa])

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
y = data['target']
X = data.drop('target', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Load mô hình đã huấn luyện
clf = DecisionTreeClassifier(max_depth=10)
clf.fit(X_train, y_train)

# Hàm dự đoán bệnh tim dựa trên dữ liệu đầu vào của người dùng
def du_doan_benh_tim(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    input_data = pd.DataFrame({
        'age': [age],
        'sex_0': [0],
        'sex_1': [0],
        'cp_0': [0],
        'cp_1': [0],
        'cp_2': [0],
        'cp_3': [0],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs_0': [0],
        'fbs_1': [0],
        'restecg_0': [0],
        'restecg_1': [0],
        'restecg_2': [0],
        'thalach': [thalach],
        'exang_0': [0],
        'exang_1': [0],
        'oldpeak': [oldpeak],
        'slope_0': [0],
        'slope_1': [0],
        'slope_2': [0],
        'ca_0': [0],
        'ca_1': [0],
        'ca_2': [0],
        'ca_3': [0],
        'ca_4': [0],
        'thal_0': [0],
        'thal_1': [0],
        'thal_2': [0],
        'thal_3': [0]
    })

    # Thiết lập giá trị mã hóa one-hot phù hợp
    input_data[f'sex_{sex}'] = 1
    input_data[f'cp_{cp}'] = 1
    input_data[f'fbs_{fbs}'] = 1
    input_data[f'restecg_{restecg}'] = 1
    input_data[f'exang_{exang}'] = 1
    input_data[f'slope_{slope}'] = 1
    input_data[f'ca_{ca}'] = 1
    input_data[f'thal_{thal}'] = 1

    # Chuẩn hóa các đặc trưng liên tục
    input_data[['age', 'trestbps', 'chol', 'thalach', 'oldpeak']] = standardScaler.transform(input_data[['age', 'trestbps', 'chol', 'thalach', 'oldpeak']])

    # Sắp xếp lại các cột để khớp với thứ tự trong quá trình huấn luyện mô hình
    input_data = input_data[X_train.columns]

    du_doan = clf.predict(input_data)
    return du_doan[0]

# Đọc dữ liệu từ tệp param.txt
with open("params.txt", "r") as file:
    # Đọc và tách các giá trị từ dòng đầu tiên
    tham_so_str = file.readline().strip()
    # Loại bỏ dấu phẩy cuối cùng (nếu có)
    if tham_so_str.endswith(','):
        tham_so_str = tham_so_str[:-1]
    # Chuyển đổi các giá trị sang kiểu số float và lưu vào danh sách
    tham_so = list(map(float, tham_so_str.split(',')))

# Gọi hàm dự đoán với các giá trị từ tệp param.txt
du_doan = du_doan_benh_tim(*tham_so)

# Ghi kết quả dự đoán vào tệp result.txt
with open("result.txt", "w") as file:
    file.write(str(du_doan))

# Tạo thêm hiển thị kết quả dự đoán
if du_doan == 1:
    print("Dự đoán: Người này có nguy cơ mắc bệnh tim.")
else:
    print("Dự đoán: Người này không có nguy cơ mắc bệnh tim.")