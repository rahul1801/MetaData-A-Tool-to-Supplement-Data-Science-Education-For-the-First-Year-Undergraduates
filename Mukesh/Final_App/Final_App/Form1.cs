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
			myComboBoxes.Add(featureEngineerDropDown);
			myComboBoxes.Add(analysisDropDown);

			// Disable submit button
			submitButton.Enabled = false;

			// Image settings
			pictureBox1.Image = Image.FromFile("E:\\IBM\\Mukesh\\Final_App\\Final_App\\Resources\\start.png");
			pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
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

				// disable text box
				filenameTextBox.Enabled = false;

				// Image settings
				pictureBox1.Image = Image.FromFile("E:\\IBM\\Mukesh\\Final_App\\Final_App\\Resources\\load_data.png");
			}
			else if(choice == "Data Info.")
			{
				// Update index
				index = 2;

				// hide label
				targetFeatureLabel.Visible = false;

				// hide data head table and label
				dataHeadLabel.Visible = false;
				headGridView.Visible = false;

				// hide info table and label
				dataInfoLabel.Visible = false;
				infoGridView.Visible = false;

				// hide numerical features table and label
				numericalListView.Visible = false;
				numericalLabel.Visible = false;

				// hide categorical features table and label
				categoricalListView.Visible = false;
				categoricalLabel.Visible = false;

				// switch to dataInfoTab
				stackPanel1.SelectedIndex = index;

				// change text of button
				submitButton.Text = "Fetch";

				// Image settings
				pictureBox1.Image = Image.FromFile("E:\\IBM\\Mukesh\\Final_App\\Final_App\\Resources\\load_data.png");
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

				// Image settings
				pictureBox1.Image = Image.FromFile("E:\\IBM\\Mukesh\\Final_App\\Final_App\\Resources\\cat_to_num.png");
			}
			else if(choice == "Missing Value Handling")
			{
				// Update index
				index = 4;

				// Switch to missingValueTab
				stackPanel1.SelectedIndex = index;

				// Image settings
				pictureBox1.Image = Image.FromFile("E:\\IBM\\Mukesh\\Final_App\\Final_App\\Resources\\mvh.png");
			}
			else if (choice == "Scaling")
			{
				// Update index
				index = 5;

				// Switch to missingValueTab
				stackPanel1.SelectedIndex = index;

				// Image settings
				pictureBox1.Image = Image.FromFile("E:\\IBM\\Mukesh\\Final_App\\Final_App\\Resources\\scaling.png");
			}
		}

		private void featureEngineerDropDown_SelectedIndexChanged(object sender, EventArgs e)
		{
			// If this is reset
			if (featureEngineerDropDown.SelectedIndex == -1)
				return;

			// Reset all other dropdowns
			for (int i = 0; i < myComboBoxes.Count(); i++)
			{
				if (i != 2)
				{
					myComboBoxes[i].SelectedIndex = -1;
				}
			}

			// Choice selected
			string choice = featureEngineerDropDown.SelectedItem.ToString();

			// Enable submit button
			submitButton.Enabled = true;

			
			if (choice == "Dimensionality Reduction")
			{
				// Update index
				index = 8;

				// Hide labels
				dimReduceResults1.Visible = false;
				dimReduceResults2.Visible = false;

				string arg = " 99";

				// Switch to loaderTab
				stackPanel1.SelectedIndex = 9;

				// Disable Submit Button
				submitButton.Enabled = false;

				// Image settings
				pictureBox1.Image = Image.FromFile("E:\\IBM\\Mukesh\\Final_App\\Final_App\\Resources\\dimreduce.png");

				backgroundWorker1.RunWorkerAsync(arg);
			}
		}

		private void analysisDropDown_SelectedIndexChanged(object sender, EventArgs e)
		{
			// If this is reset
			if (analysisDropDown.SelectedIndex == -1)
				return;

			// Reset all other dropdowns
			for (int i = 0; i < myComboBoxes.Count(); i++)
			{
				if (i != 3)
				{
					myComboBoxes[i].SelectedIndex = -1;
				}
			}

			// Choice selected
			 string choice = analysisDropDown.SelectedItem.ToString();

			// Enable submit button
			submitButton.Enabled = true;

			if (choice == "Noise Detection")
			{
				// Update index
				index = 6;

				// hide label
				noiseDetectLabel.Visible = false;

				// hide ListView
				noisyListView.Visible = false;

				// switch to noiseDetectTab
				stackPanel1.SelectedIndex = index;

				// change text of button
				submitButton.Text = "Perform";

				// Image settings
				pictureBox1.Image = Image.FromFile("E:\\IBM\\Mukesh\\Final_App\\Final_App\\Resources\\noise.png");
			}
			else if (choice == "Multi-Collinearity Analysis")
			{
				// Update index
				index = 7;

				// hide label
				mcaLabel.Visible = false;

				// hide corrLabel
				corrLabel.Visible = false;

				// hide corrGrid
				corrGridView.Visible = false;

				// switch to mcaTab
				stackPanel1.SelectedIndex = index;

				// change text of button
				submitButton.Text = "Perform";

				// Image settings
				pictureBox1.Image = Image.FromFile("E:\\IBM\\Mukesh\\Final_App\\Final_App\\Resources\\mca.png");
			}
			else if (choice == "Regressional Analysis")
			{
				// Update index
				index = 10;

				// switch to regTab
				stackPanel1.SelectedIndex = index;

				// change text of button
				submitButton.Text = "Perform";

				// Image settings
				pictureBox1.Image = Image.FromFile("E:\\IBM\\Mukesh\\Final_App\\Final_App\\Resources\\reg.png");
			}
			else if (choice == "Visualization")
			{
				// Update index
				index = 11;

				// switch to regTab
				stackPanel1.SelectedIndex = index;

				// change text of button
				submitButton.Text = "Perform";

				// Image settings
				pictureBox1.Image = Image.FromFile("E:\\IBM\\Mukesh\\Final_App\\Final_App\\Resources\\viz.png");
			}
		}

		private void submitButton_Click(object sender, EventArgs e)
		{
			if(index == 1)
			{
				// Get entered filename
				string filename = filenameTextBox.Text;

				// Get nature of y
				string n_y = "";
				if(numericalRadio.Checked)
				{
					n_y = " 1";
				}
				else if(categoricalRadio.Checked)
				{
					n_y = " 0";
				}

				// Argument to the script
				string arg = " 0 " + filename + n_y;

				// Start the asynchronous operation.
				backgroundWorker1.RunWorkerAsync(arg);
			}
			else if(index == 2)
			{
				// Argument to the script
				string arg = " 1";

				// Switch to loaderTab
				stackPanel1.SelectedIndex = 9;

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
			else if(index==4)
			{
				// Argument to the script
				string arg = " 3 ";

				// Assign argument correspondingly;
				if (meanRadio.Checked)
				{
					arg += "1";
				}
				else if (medianRadio.Checked)
				{
					arg += "2";
				}
				else if(modeRadio.Checked)
				{
					arg += "3";
				}

				// Start the asynchronous operation.
				backgroundWorker1.RunWorkerAsync(arg);
			}
			else if (index == 5)
			{
				// Argument to the script
				string arg = " 4 ";

				// Assign argument correspondingly;
				if (zScoreRadio.Checked)
				{
					arg += "1";
				}
				else if (minMaxRadio.Checked)
				{
					arg += "2";
				}

				// Start the asynchronous operation.
				backgroundWorker1.RunWorkerAsync(arg);
			}
			else if (index == 6)
			{
				// Argument to the script
				string arg = " 6";

				// Switch to loaderTab
				stackPanel1.SelectedIndex = 9;

				// Start the asynchronous operation.
				backgroundWorker1.RunWorkerAsync(arg);
			}
			else if (index == 7)
			{
				// Argument to the script
				string arg = " 5";

				// Start the asynchronous operation.
				backgroundWorker1.RunWorkerAsync(arg);
			}
			else if (index == 8)
			{
				// Argument to the script
				string arg = " 7 ";

				// Assign argument correspondingly;
				if (pcaRadio.Checked)
				{
					arg += "1 ";
				}
				else if (autoencoderRadio.Checked)
				{
					arg += "2 ";
				}

				// Desired no of features
				arg += dimrReduceNumber.Value.ToString();

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
				Console.WriteLine(prompt);
			}

			// Success
			else
			{
				// Get result - <output of program,arguments>
				KeyValuePair<string, string> result = (KeyValuePair<string, string>)e.Result;
				if(result.Value == " 1")
				{
					// write info table
					bindCSV("E:\\IBM\\Mukesh\\Entry_data\\info.csv", infoGridView, 1);

					// write head table
					bindCSV("E:\\IBM\\Mukesh\\Entry_data\\head.csv", headGridView, 1);

					// write numerical features and categorical features
					string[] res_split = result.Key.Split('!');
					string[] num_features = res_split[0].Split('\n');
					string[] cat_features = res_split[1].Split('\n');
					numericalListView.Items.Clear();
					numericalListView.Columns[0].Width = numericalListView.Width - 4;
					for(int i=0;i<num_features.Length;i++)
					{
						numericalListView.Items.Add(num_features[i], i);
					}
					categoricalListView.Items.Clear();
					categoricalListView.Columns[0].Width = categoricalListView.Width - 4;
					for (int i = 0; i < cat_features.Length; i++)
					{
						categoricalListView.Items.Add(cat_features[i], i);
					}

					// write name of target feature
					targetFeatureLabel.Text = res_split[2];

					// change text of button
					submitButton.Text = "Submit";

					// show target feature
					targetFeatureLabel.Visible = true;

					// show data head table and label
					dataHeadLabel.Visible = true;
					headGridView.Visible = true;

					// show info table and label
					dataInfoLabel.Visible = true;
					infoGridView.Visible = true;

					// show numerical features table and label
					numericalListView.Visible = true;
					numericalLabel.Visible = true;

					// show categorical features table and label
					categoricalListView.Visible = true;
					categoricalLabel.Visible = true;

					// Switch to dataInfoTab
					stackPanel1.SelectedIndex = 2;
				}
				else if(result.Value == " 5")
				{
					// write and show label
					mcaLabel.Text = result.Key;
					mcaLabel.Visible = true;

					// write corr matrix
					bindCSV("E:\\IBM\\Mukesh\\Entry_data\\corr.csv", corrGridView, 2);

					// show corrLabel and corr matrix
					corrGridView.Visible = true;
					corrGridView.Visible = true;

					// change text of button
					submitButton.Text = "Submit";
				}
				else if (result.Value == " 6")
				{
					// Show label
					noiseDetectLabel.Visible = true;

					string[] noise_info = result.Key.Split('!');
					if(noise_info.Length == 1)
					{
						// write label for no noise
						noiseDetectLabel.Text = result.Key;
					}
					else
					{
						// write label for noise
						noiseDetectLabel.Text = noise_info[0];

						// write ListView
						string[] noisy_features = noise_info[1].Split('\n');
						noisyListView.Items.Clear();
						noisyListView.Columns[0].Width = noisyListView.Width - 4;

						// Avoid last extra line
						for (int i = 0; i < (noisy_features.Length - 1); i++)
						{
							noisyListView.Items.Add(noisy_features[i], i);
						}

						// show ListView
						noisyListView.Visible = true;
					}

					// switch to noiseDetectTab
					stackPanel1.SelectedIndex = 6;

					// change text of button
					submitButton.Text = "Submit";
				}
				else if (result.Value == " 99")
				{
					// get total number of features in data
					int num_features = Int32.Parse(result.Key);
					dimrReduceNumber.Value = num_features;
					dimrReduceNumber.Maximum = num_features;

					// Switch to dimReduceTab
					stackPanel1.SelectedIndex = 8;

					// Enable submit button
					submitButton.Enabled = true;
					return;
				}
				else if (result.Value.Substring(0,2) == " 7")
				{
					// Fill and show labels
					string[] res = result.Key.Split('\n');
					string label_text = "\t\u2022" + res[0];
					dimReduceResults1.Text = label_text;
					dimReduceResults1.Visible = true;
					dimReduceResults2.Text = "\t\u2022" + res[1];
					dimReduceResults2.Visible = true;
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
			string python = @"python.exe";

			// python app to call 
			string myPythonApp = @"..\..\..\..\Data_menu_driven.py";

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

		private void fileLoadButton_Click(object sender, EventArgs e)
		{
			DialogResult result = openFileDialog1.ShowDialog();
			if(result==DialogResult.OK)
			{
				string file_name = openFileDialog1.FileName;
				filenameTextBox.Text = file_name;
			}
		}

		// Parses a csv file and displays it to a DataGridView
		// rowHeaderChoice is 0 if no header, 1 if row numbers, 2 if row names
		// if rowHeaderChoice is 2 and names is left null, row headers and column headers are same
		private void bindCSV(string filePath, DataGridView dgv, int rowHeaderChoice, string[] names=null)
		{
			DataTable dt = new DataTable();
			string[] lines = System.IO.File.ReadAllLines(filePath);
			if(lines.Length > 0)
			{
				// first line to create header
				string firstLine = lines[0];

				string[] headerLabels = firstLine.Split(',');

				foreach(string hword in headerLabels)
				{
					dt.Columns.Add(new DataColumn(hword));
				}

				// data
				for(int r=1;r<lines.Length;r++)
				{
					string[] dwords = lines[r].Split(',');
					DataRow dr = dt.NewRow();
					int colIndex = 0;
					foreach(string hword in headerLabels)
					{
						dr[hword] = dwords[colIndex++];
					}
					dt.Rows.Add(dr);
				}
			}
			if(dt.Rows.Count>0)
			{
				dgv.DataSource = dt;
				if(rowHeaderChoice == 1)
				{
					setRowNumber(dgv);
				}
				else if(rowHeaderChoice==2)
				{
					if (names == null)
						setRowNames(dgv, lines[0].Split(','));
					else
						setRowNames(dgv, names);
				}
				else
				{
					dgv.RowHeadersVisible = false; 
				}
			}
		}

		// Displays row number
		private void setRowNumber(DataGridView dgv)
		{
			foreach (DataGridViewRow row in dgv.Rows)
			{
				row.HeaderCell.Value = (row.Index + 1).ToString();
				Console.Write(row.HeaderCell.Value);
				Console.WriteLine(row.HeaderCell.Visible);
			}
		}

		// Displays given list as row headers
		private void setRowNames(DataGridView dgv, string[] names)
		{
			int i = 0;
			foreach (DataGridViewRow row in dgv.Rows)
			{
				row.HeaderCell.Value = names[i];
				Console.WriteLine(names[i]);
				i++;
			}
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
