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

namespace Final_App
{
	public partial class Final_App : Form
	{
		public Final_App()
		{
			InitializeComponent();
		}

		// list of panels
		List<Panel> panelList = new List<Panel>();

		// index of panel being shown
		int index = 0;

		ProcessStartInfo myProcessStartInfo;

		Process myProcess;

		private void Final_App_Load(object sender, EventArgs e)
		{
			// add panels to list
			panelList.Add(panel1);
			panelList.Add(panel2);
			panelList[index].BringToFront();

			// full path of python interpreter 
			string python = @"C:\Users\Mukesh Chugani\Anaconda3\python.exe";

			// python app to call 
			string myPythonApp = @"E:\IBM\Mukesh\prac.py";


			// Create new process start info 
			myProcessStartInfo = new ProcessStartInfo(python);

			// make sure we can read the output from stdout 
			myProcessStartInfo.UseShellExecute = false;
			myProcessStartInfo.RedirectStandardOutput = true;
			myProcessStartInfo.RedirectStandardInput = true;
			myProcessStartInfo.CreateNoWindow = true;

			// arguments
			myProcessStartInfo.Arguments = myPythonApp + " -u";

			myProcess = new Process();

			// assign start information to the process 
			myProcess.StartInfo = myProcessStartInfo;
		}

		private void startButton_Click(object sender, EventArgs e)
		{

			// start the process 
			myProcess.Start();

			// Read the standard output of the app.
			StreamReader myStreamReader = myProcess.StandardOutput;
			string myString = "";

			while (!myStreamReader.EndOfStream)
			{
				String s = myStreamReader.ReadLine();
				if (s != "")
				{
					myString += s+'\n';
					// Console.WriteLine(s);
				}
			}
			Console.WriteLine(myString);
			// Show Welcome text
			welcomeLabel.Text = myString;


			// Change the panel
			panelList[index].Hide();
			panelList[++index].Show();
			myProcess.Close();
		}

		private void enterUrlButton_Click(object sender, EventArgs e)
		{

		}
	}
}
