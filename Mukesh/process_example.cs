using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Trial1
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private void startButton_Click(object sender, EventArgs e)
		{
			// full path of python interpreter 
			string python = @"C:\Users\Mukesh Chugani\Anaconda3\python.exe";

			// python app to call 
			string myPythonApp = @"E:\sum.py";

			// dummy parameters to send Python script 
			int x = 2;
			int y = 5;

			// Create new process start info 
			ProcessStartInfo myProcessStartInfo = new ProcessStartInfo(python);

			// make sure we can read the output from stdout 
			myProcessStartInfo.UseShellExecute = false;
			myProcessStartInfo.RedirectStandardOutput = true;
			myProcessStartInfo.RedirectStandardInput = true;
			// start python app with 3 arguments  
			// 1st arguments is pointer to itself,  
			// 2nd and 3rd are actual arguments we want to send 
			myProcessStartInfo.Arguments = myPythonApp + " " + x + " " + y;

			Process myProcess = new Process();
			// assign start information to the process 
			myProcess.StartInfo = myProcessStartInfo;
			

			Console.WriteLine("Calling Python script with arguments {0} and {1}", x, y);
			// start the process 
			myProcess.Start();

			// Read the standard output of the app we called.  
			// in order to avoid deadlock we will read output first 
			// and then wait for process terminate: 
			StreamReader myStreamReader = myProcess.StandardOutput;
			string myString = myStreamReader.ReadLine();

			/*if you need to read multiple lines, you might use: 
                string myString = myStreamReader.ReadToEnd() */

			// wait exit signal from the app we called and then close it. 
			StreamWriter streamWriter = myProcess.StandardInput;
			streamWriter.WriteLine("2 6");

			string myString2 = myStreamReader.ReadLine();
			myProcess.Close();

			// write the output we got from python app 
			label1.Text = "Value received from script: " + myString2;
			Console.WriteLine();
		}
	}
}
