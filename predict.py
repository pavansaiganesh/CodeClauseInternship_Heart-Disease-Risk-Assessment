import joblib 

rf = joblib.load('filename2.pkl') 

"""eg:  arr = [[6.40e+01, 1.00e+00, 0.00e+00, 1.28e+02, 2.63e+02, 0.00e+00,
       1.00e+00, 1.05e+02, 1.00e+00, 2.00e-01, 1.00e+00, 1.00e+00,
       3.00e+00]]"""

def predict_type(arr):
    res = rf.predict(arr)
    print(res)
    if res == 0:
        return 'You dont have a heart disease :)'
    return 'Sorry! You have a heart disease'
    