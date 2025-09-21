# 🚀 **MANUAL STARTUP GUIDE**

## **Step-by-Step Instructions to Run Your Project Management Tool**

### **STEP 1: Start Backend Server**

1. **Open Command Prompt or PowerShell**
2. **Navigate to the backend directory:**
   ```bash
   cd C:\1_PROFESSIONAL\Projects\Project_Management_Tool\backend
   ```

3. **Activate the virtual environment:**
   ```bash
   venv\Scripts\activate.bat
   ```

4. **Start the backend server:**
   ```bash
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Wait for this message:**
   ```
   INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
   INFO:     Application startup complete.
   ```

### **STEP 2: Start Frontend Server (New Terminal)**

1. **Open a NEW Command Prompt or PowerShell window**
2. **Navigate to the frontend directory:**
   ```bash
   cd C:\1_PROFESSIONAL\Projects\Project_Management_Tool\frontend
   ```

3. **Start the frontend server:**
   ```bash
   npm start
   ```

4. **Wait for this message:**
   ```
   webpack compiled with 0 errors
   Local:            http://localhost:3000
   On Your Network:  http://192.168.x.x:3000
   ```

### **STEP 3: Access Your Application**

1. **Open your web browser**
2. **Go to:** http://localhost:3000
3. **Register your first account**
4. **Start using your Project Management Tool!**

## **Alternative: Use the Batch Files**

### **Option 1: Automatic Setup**
- **Double-click `setup_and_run.bat`**

### **Option 2: Quick Start**
- **Double-click `start_all.bat`**

## **Troubleshooting**

### **If Backend Won't Start:**
- Make sure you're in the `backend` directory
- Ensure virtual environment is activated (you should see `(venv)` in your prompt)
- Check if port 8000 is available

### **If Frontend Won't Start:**
- Make sure you're in the `frontend` directory
- Run `npm install` if dependencies are missing
- Check if port 3000 is available

### **If You Get Import Errors:**
- Make sure the virtual environment is activated
- Run: `pip install -r requirements.txt`

## **Access Points**

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/monitoring/health

## **What You Can Do**

- ✅ **User Registration/Login**
- ✅ **Create and Manage Projects**
- ✅ **Create and Assign Tasks**
- ✅ **Track Time**
- ✅ **Upload Files**
- ✅ **Real-time Updates**
- ✅ **Advanced Search**
- ✅ **Dark Mode**
- ✅ **Email Notifications**

**Your Project Management Tool is ready to use! 🎉**
