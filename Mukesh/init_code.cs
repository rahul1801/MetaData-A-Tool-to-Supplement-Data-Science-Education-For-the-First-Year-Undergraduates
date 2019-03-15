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

namespace Final_Application
{
	public partial class Form1 : Form
	{
		// list of panels
		List<Panel> listPanel = new List<Panel>();
		
		// index of panel being shown
		int index = 0;

		public Form1()
		{
			InitializeComponent();
		}

		private void Form1_Load(object sender, EventArgs e)
		{

			// add panels to list
			listPanel.Add(panel1);
			listPanel.Add(panel2);
			listPanel[index].BringToFront();

			// don't show anything at the beginning
			welcomeLabel.Visible = false;
			urlTextBox.Visible = false;
		}

		private void startButton_Click(object sender, EventArgs e)
		{
			// full path of python interpreter 
			string python = @"C:\Users\Mukesh Chugani\Anaconda3\python.exe";

			// python app to call 
			string myPythonApp = @"E:\IBM\Mukesh\Data_menu_driven.py";

			// Create new process start info 
			ProcessStartInfo myProcessStartInfo = new ProcessStartInfo(python);

			// make sure we can read the output from stdout 
			myProcessStartInfo.UseShellExecute = false;
			myProcessStartInfo.RedirectStandardOutput = true;
			myProcessStartInfo.RedirectStandardInput = true;

			// arguments
			myProcessStartInfo.Arguments = myPythonApp;

			Process myProcess = new Process();

			// assign start information to the process 
			myProcess.StartInfo = myProcessStartInfo;

			// start the process 
			myProcess.Start();

			// Read the standard output of the app.
			StreamReader myStreamReader = myProcess.StandardOutput;
			string myString = myStreamReader.ReadToEnd();

			// show welcome text and hide start button
			startButton.Visible = false;
			welcomeLabel.Visible = true;
			welcomeLabel.Text = myString;
			urlTextBox.Visible = true;

			// get url from textbox
			string file_path = urlTextBox.Text;

			// feed path to the app
			StreamWriter streamWriter = myProcess.StandardInput;
			streamWriter.WriteLine(file_path);

			// read output from the app
			myString = myStreamReader.ReadToEnd();

			// bring next panel to the front
			listPanel[++index].BringToFront();

			// write label
			dataInfoLabel.Text = myString;


		}
	}
}
