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
	public partial class Final_Application : Form
	{

		// list of dropdowns
		List<ComboBox> myComboBoxes = new List<ComboBox>();

		// present tab
		int index = 1;

		public Final_Application()
		{
			InitializeComponent();
		}

		private void Final_Application_Load(object sender, EventArgs e)
		{ 
			// Add dropdowns to list
			myComboBoxes.Add(dataInputDropDown);
			myComboBoxes.Add(preProcessDropDown);

			// Disable submit button
			submitButton.Enabled = false;
		}

		private void dataInputDropDown_SelectedIndexChanged(object sender, EventArgs e)
		{

			// If this is reset
			if (dataInputDropDown.SelectedIndex == -1)
				return;

			// Reset all other dropdowns
			for (int i = 0; i < myComboBoxes.Count(); i++)
			{
				if (i != 0)
				{
					myComboBoxes[i].SelectedIndex = -1;
				}
			}

			// Choice selected
			string choice = dataInputDropDown.SelectedItem.ToString();

			// Enable submit button
			submitButton.Enabled = true;

			if (choice == "Load Data")
			{
				// Update index
				index = 1;

				// switch to loadDataTab
				stackPanel1.SelectedIndex = index;
			}
			else if(choice == "Data Info.")
			{
				// Update index
				index = 2;

				// hide label
				dataInfoLabel.Visible = false;

				// switch to dataInfoTab
				stackPanel1.SelectedIndex = index;

				// change text of button
				submitButton.Text = "Load";
			}
		}

		private void preProcessDropDown_SelectedIndexChanged(object sender, EventArgs e)
		{
			// If this is reset
			if (preProcessDropDown.SelectedIndex == -1)
				return;

			// Reset all other dropdowns
			for (int i = 0; i < myComboBoxes.Count(); i++)
			{
				if (i != 1)
				{
					myComboBoxes[i].SelectedIndex = -1;
				}
			}

			// Choice selected
			string choice = preProcessDropDown.SelectedItem.ToString();

			// Enable submit button
			submitButton.Enabled = true;

			if (choice == "Categorical to Numerical Conversion")
			{
				// Update index
				index = 3;

				// Switch to catToNumTab
				stackPanel1.SelectedIndex = index;
			}
		}

		private void submitButton_Click(object sender, EventArgs e)
		{
			if(index == 1)
			{
				// Get entered filename
				string filename = filenameTextBox.Text;

				// Argument to the script
				string arg = " 0 " + filename;

				// Start the asynchronous operation.
				backgroundWorker1.RunWorkerAsync(arg);
			}
			else if(index == 2)
			{
				// Argument to the script
				string arg = " 1";

				// Start the asynchronous operation.
				backgroundWorker1.RunWorkerAsync(arg);
			}
			else if(index==3)
			{
				// Argument to the script
				string arg = " 2 ";

				// Assign argument correspondingly;
				if (labelEncodingRadio.Checked)
				{
					arg += "1";
				}
				else if(oneHotRadio.Checked)
				{
					arg += "2";
				}

				// Start the asynchronous operation.
				backgroundWorker1.RunWorkerAsync(arg);
			}
		}

		private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
		{
			// Get the BackgroundWorker that raised this event.
			BackgroundWorker worker = sender as BackgroundWorker;

			// Assign the result of the computation
			// to the Result property of the DoWorkEventArgs
			// object. This will be available to the 
			// RunWorkerCompleted eventhandler.
			e.Result = callProcess((string)e.Argument, worker, e);
		}

		private void backgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
		{
			// Prompt text
			string prompt;

			// Error
			if (e.Error != null)
			{
				prompt = e.Error.Message;
			}

			// Success
			else
			{
				// Get result - <output of program,arguments>
				KeyValuePair<string, string> result = (KeyValuePair<string, string>)e.Result;
				if(result.Value == " 1")
				{
					// write and show label
					dataInfoLabel.Text = result.Key;
					dataInfoLabel.Visible = true;

					// change text of button
					submitButton.Text = "Submit";
				}
				else
				{
					// Show Prompt
					MessageBox.Show(result.Key);
				}
			}
			// Disable further action
			submitButton.Enabled = false;
		}

		KeyValuePair<string, string> callProcess(string arg, BackgroundWorker worker, DoWorkEventArgs e)
		{
			string myString = "";

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
			myProcessStartInfo.Arguments = myPythonApp + arg;

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
				}
			}
			KeyValuePair<string, string> result = new KeyValuePair<string, string>(myString, arg);
			return result;
		}
	}

	class StackPanel : TabControl
	{
		protected override void WndProc(ref Message m)
		{
			// Hide tabs by trapping the TCM_ADJUSTRECT message
			if (m.Msg == 0x1328 && !DesignMode) m.Result = (IntPtr)1;
			else base.WndProc(ref m);
		}
	}
}
