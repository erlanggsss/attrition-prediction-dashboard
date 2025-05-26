import pandas as pd
import joblib

# Fungsi untuk memuat model dan melakukan prediksi
def load_model_and_predict(model_path, data):
    """
    Memuat model dari file .pkl dan melakukan prediksi berdasarkan input data.
    
    Args:
        model_path (str): Lokasi file model .pkl.
        data (pd.DataFrame): Data input untuk prediksi.

    Returns:
        predictions (array): Prediksi model berdasarkan data input.
    """
    # Memuat model dari file .pkl
    model = joblib.load(model_path)
    
    # Melakukan prediksi menggunakan model yang telah dimuat
    predictions = model.predict(data)
    
    return predictions

# Fungsi utama untuk menjalankan prediksi
def main():
    """
    Fungsi utama yang menerima input pengguna dan memprediksi kemungkinan attrition.
    
    Fitur yang diminta untuk input:
    - Age: Umur karyawan (misalnya: 34)
    - BusinessTravel: Frekuensi perjalanan bisnis (1 = Rarely, 2 = Frequently, 3 = Non-Travel)
    - DailyRate: Tarif harian dalam angka (misalnya: 800)
    - Department: Departemen kerja (1 = HR, 2 = R&D, 3 = Sales)
    - DistanceFromHome: Jarak dari rumah dalam kilometer (misalnya: 10)
    - Education: Tingkat pendidikan (1 = High School, 2 = College, 3 = Bachelor, 4 = Master, 5 = PhD)
    - EducationField: Bidang pendidikan (0 = Other, 1 = Medical, 2 = Life Sciences, 3 = Marketing, 4 = Technical Degree, 5 = HR)
    - EnvironmentSatisfaction: Tingkat kepuasan lingkungan kerja (1-4)
    - Gender: Jenis kelamin (0 = Female, 1 = Male)
    - JobRole: Posisi pekerjaan (1 = HR, 2 = Healthcare Representative, 3 = Research Scientist, 4 = Sales Executive, 5 = Manager, 
      6 = Laboratory Technician, 7 = Research Director, 8 = Manufacturing Director, 9 = Sales Representative)
    - MaritalStatus: Status pernikahan (1 = Married, 2 = Single, 3 = Divorced)
    - OverTime: Apakah karyawan bekerja lembur (1 = Yes, 0 = No)
    - PerformanceRating: Penilaian kinerja (1-5)
    - RelationshipSatisfaction: Kepuasan hubungan kerja (1-4)
    - StockOptionLevel: Level opsi saham (0-3)
    - TotalWorkingYears: Total tahun bekerja
    - TrainingTimesLastYear: Jumlah pelatihan yang diterima tahun lalu
    - WorkLifeBalance: Keseimbangan kerja-hidup (1-4)
    - YearsAtCompany: Tahun bekerja di perusahaan saat ini
    - YearsInCurrentRole: Tahun bekerja di posisi saat ini
    - YearsSinceLastPromotion: Tahun sejak promosi terakhir
    - YearsWithCurrManager: Tahun bekerja dengan manajer saat ini
    - HourlyRate: Tarif per jam
    - JobInvolvement: Keterlibatan pekerjaan (1 = Low, 2 = Medium, 3 = High)
    - JobLevel: Level pekerjaan (1 = Entry Level, 2 = Junior, 3 = Mid Level, 4 = Senior)
    - JobSatisfaction: Kepuasan kerja (1 = Very Dissatisfied, 2 = Dissatisfied, 3 = Neutral, 4 = Satisfied, 5 = Very Satisfied)
    - MonthlyIncome: Pendapatan bulanan
    - MonthlyRate: Tarif bulanan
    - NumCompaniesWorked: Jumlah perusahaan tempat bekerja sebelumnya
    - PercentSalaryHike: Persentase kenaikan gaji
    """
    # Input data baru (misalnya, data yang diberikan oleh pengguna)
    new_employee_raw = pd.DataFrame({
    'Age': [34],
    'BusinessTravel': [1],
    'DailyRate': [800],
    'Department': [2],
    'DistanceFromHome': [10],
    'Education': [3],
    'EducationField': [2],
    'EnvironmentSatisfaction': [3],
    'Gender': [1],
    'HourlyRate': [60],
    'JobInvolvement': [3],
    'JobLevel': [2],
    'JobRole': [2],
    'JobSatisfaction': [4],
    'MaritalStatus': [2],
    'MonthlyIncome': [7000],
    'MonthlyRate': [14000],
    'NumCompaniesWorked': [1],
    'OverTime': [1],
    'PercentSalaryHike': [15],
    'RelationshipSatisfaction': [2],
    'StockOptionLevel': [1],
    'TotalWorkingYears': [10],
    'TrainingTimesLastYear': [2],
    'WorkLifeBalance': [3],
    'YearsAtCompany': [5],
    'YearsInCurrentRole': [3],
    'YearsSinceLastPromotion': [1],
    'YearsWithCurrManager': [2]
    })

    # Fitur yang digunakan pada model (harus sesuai dengan data yang digunakan saat pelatihan)
    features = ['Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome', 'Education', 
                'EducationField', 'EnvironmentSatisfaction', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime', 
                'RelationshipSatisfaction', 'StockOptionLevel', 'TotalWorkingYears', 'YearsSinceLastPromotion', 
                'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole', 
                'YearsWithCurrManager', 'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobSatisfaction', 
                'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'PercentSalaryHike']

    # Menyesuaikan input dengan fitur yang digunakan dalam model
    new_employee_raw = new_employee_raw[features].values

    # Memuat model yang sudah disimpan (RF dan LR)
    rf_model_path = './models/rf_model.pkl'  
    lr_model_path = './models/lr_model.pkl'  
    
    # Prediksi dengan Random Forest
    rf_predictions = load_model_and_predict(rf_model_path, new_employee_raw)
    
    # Prediksi dengan Logistic Regression
    lr_predictions = load_model_and_predict(lr_model_path, new_employee_raw)
    
    # Menampilkan hasil prediksi
    print("\nHasil Prediksi Attrition:")
    print(f"Prediksi Random Forest (RF): {'Attrition' if rf_predictions[0] == 1 else 'Tidak Attrition'}")
    print(f"Prediksi Logistic Regression (LR): {'Attrition' if lr_predictions[0] == 1 else 'Tidak Attrition'}\n")

if __name__ == "__main__":
    main()