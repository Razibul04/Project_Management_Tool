# 🚀 **SIMPLE STARTUP GUIDE - WORKING SOLUTION**

## **EASIEST METHOD: Use the Working Batch File**

**Double-click `WORKING_STARTUP.bat`** - This will start both servers in separate windows!

## **MANUAL METHOD: Step by Step**

### **Step 1: Start Backend**

1. **Open Command Prompt**
2. **Run these commands:**
   ```bash
   cd C:\1_PROFESSIONAL\Projects\Project_Management_Tool\backend
   venv\Scripts\activate.bat
   python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

3. **Wait for:**
   ```
   INFO:     Application startup complete.
   INFO:     Uvicorn running on http://127.0.0.1:8000
   ```

### **Step 2: Start Frontend (New Terminal)**

1. **Open NEW Command Prompt**
2. **Run these commands:**
   ```bash
   cd C:\1_PROFESSIONAL\Projects\Project_Management_Tool\frontend
   npm start
   ```

3. **Wait for:**
   ```
   webpack compiled with 0 errors
   Local:            http://localhost:3000
   ```

### **Step 3: Access Your App**

1. **Open browser**
2. **Go to:** http://localhost:3000
3. **Register and start using!**

## **Access Points**

- **Frontend**: http://localhost:3000
- **Backend**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs

## **What You Can Do**

- ✅ **User Registration/Login**
- ✅ **Create Projects**
- ✅ **Manage Tasks**
- ✅ **Time Tracking**
- ✅ **File Uploads**
- ✅ **Real-time Updates**
- ✅ **Dark Mode**
- ✅ **Advanced Search**

## **Troubleshooting**

### **If Backend Won't Start:**
- Make sure you're in the `backend` directory
- Ensure virtual environment is activated (you should see `(venv)` in prompt)
- Try: `pip install -r requirements.txt`

### **If Frontend Won't Start:**
- Make sure you're in the `frontend` directory
- Try: `npm install`

## **Success!**

Your Project Management Tool is ready! Just follow the steps above and you'll be up and running! 🎉
