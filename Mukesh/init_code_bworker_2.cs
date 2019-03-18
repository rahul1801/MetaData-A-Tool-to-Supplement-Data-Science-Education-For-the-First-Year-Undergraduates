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
	public partial class Form1 : Form
	{
		List<Label> myList = new List<Label>();
		int index = 0;

		public Form1()
		{
			InitializeComponent();
		}

		private void startAsyncButton_Click(object sender, EventArgs e)
		{
			// Start the asynchronous operation.
			backgroundWorker1.RunWorkerAsync(1);
		}

		string callProcess(BackgroundWorker worker, DoWorkEventArgs e)
		{
			string myString = "";
			if (worker.CancellationPending)
			{
				e.Cancel = true;
			}
			else
			{
				ProcessStartInfo myProcessStartInfo;

				Process myProcess;
				// full path of python interpreter 
				string python = @"C:\Users\Mukesh Chugani\Anaconda3\python.exe";

				// python app to call 
				string myPythonApp = @"E:\IBM\Mukesh\Data_menu_driven.py";


				// Create new process start info 
				myProcessStartInfo = new ProcessStartInfo(python);

				// make sure we can read the output from stdout 
				myProcessStartInfo.UseShellExecute = false;
				myProcessStartInfo.RedirectStandardOutput = true;
				myProcessStartInfo.RedirectStandardInput = true;
				myProcessStartInfo.CreateNoWindow = true;

				// arguments
				myProcessStartInfo.Arguments = myPythonApp + " " + "0" + " " + @"E:\IBM\Mukesh\housing.csv";

				myProcess = new Process();

				// assign start information to the process 
				myProcess.StartInfo = myProcessStartInfo;

				// start the process 
				myProcess.Start();

				// Read the standard output of the app.
				StreamReader myStreamReader = myProcess.StandardOutput;

				while (!myStreamReader.EndOfStream)
				{
					String s = myStreamReader.ReadLine();
					if (s != "")
					{
						myString += s + '\n';
						// Console.WriteLine(s);
					}
				}
			}
			return myString;
		}

		private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
		{
			// Get the BackgroundWorker that raised this event.
			BackgroundWorker worker = sender as BackgroundWorker;

			// Assign the result of the computation
			// to the Result property of the DoWorkEventArgs
			// object. This is will be available to the 
			// RunWorkerCompleted eventhandler.
			e.Result = callProcess(worker, e);
		}

		private void backgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
		{
			// First, handle the case where an exception was thrown.
			if (e.Error != null)
			{
				MessageBox.Show(e.Error.Message);
			}
			else if (e.Cancelled)
			{
				// Next, handle the case where the user canceled 
				// the operation.
				// Note that due to a race condition in 
				// the DoWork event handler, the Cancelled
				// flag may not have been set, even though
				// CancelAsync was called.
				label1.Text = "Canceled";
			}
			else
			{
				// Finally, handle the case where the operation 
				// succeeded.
				myList[index++].Text = e.Result.ToString();
			}
		}

		private void Form1_Load(object sender, EventArgs e)
		{
			myList.Add(label1);
			myList.Add(label2);
		}
	}
}
