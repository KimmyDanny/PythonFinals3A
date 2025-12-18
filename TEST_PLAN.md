
---

# 📋 TEST_PLAN.md

```md
# Test Plan – OrangeHRM Automation Testing

## 1. Introduction
This test plan describes the automated testing approach for the OrangeHRM demo application.  
The focus is on validating login functionality and basic dashboard navigation using Selenium and pytest.

## 2. Test Objectives
- Verify successful login with valid credentials
- Validate error handling for invalid login attempts
- Ensure required field validations are displayed
- Confirm Quick Launch navigation works correctly

## 3. Test Environment
- Operating System: Windows
- Browser: Google Chrome
- Automation Tool: Selenium WebDriver
- Test Framework: pytest
- Programming Language: Python

## 4. Test Scenarios

### 4.1 Positive Login Test
**Test Case ID:** TC_01  
**Description:** Login with valid username and password  
**Steps:**
1. Open OrangeHRM login page
2. Enter valid username
3. Enter valid password
4. Click Login button  
**Expected Result:** User is redirected to the dashboard

---

### 4.2 Negative Login – Invalid Password
**Test Case ID:** TC_02  
**Description:** Login with valid username and invalid password  
**Expected Result:** Error message "Invalid credentials" is displayed

---

### 4.3 Negative Login – Empty Username
**Test Case ID:** TC_03  
**Description:** Login with empty username and valid password  
**Expected Result:** "Required" validation message is displayed

---

### 4.4 Negative Login – Empty Password
**Test Case ID:** TC_04  
**Description:** Login with valid username and empty password  
**Expected Result:** "Required" validation message is displayed

---

### 4.5 Negative Login – Empty Username and Password
**Test Case ID:** TC_05  
**Description:** Login with empty username and empty password  
**Expected Result:** "Required" validation messages are displayed

---

### 4.6 Quick Launch – My Leave
**Test Case ID:** TC_06  
**Description:** Navigate to My Leave using Quick Launch  
**Steps:**
1. Login with valid credentials
2. Click My Leave from Quick Launch  
**Expected Result:** My Leave page opens successfully

## 5. Test Data
- Valid Username: Admin
- Valid Password: admin123
- Invalid Password: wrongpass
- Invalid Username: wronguser

## 6. Test Execution
- Tests are executed using pytest
- Each test runs in a fresh browser session
- Browser is closed after each test execution

## 7. Conclusion
This test plan ensures core login and navigation features of OrangeHRM are tested using basic Selenium automation.
