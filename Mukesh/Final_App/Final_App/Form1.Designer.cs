namespace Final_App
{
	partial class Final_Application
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.tableLayoutPanel1 = new System.Windows.Forms.TableLayoutPanel();
			this.flowLayoutPanel1 = new System.Windows.Forms.FlowLayoutPanel();
			this.groupBox2 = new System.Windows.Forms.GroupBox();
			this.dataInputDropDown = new System.Windows.Forms.ComboBox();
			this.groupBox1 = new System.Windows.Forms.GroupBox();
			this.preProcessDropDown = new System.Windows.Forms.ComboBox();
			this.flowLayoutPanel2 = new System.Windows.Forms.FlowLayoutPanel();
			this.submitButton = new System.Windows.Forms.Button();
			this.emptyPanel = new System.Windows.Forms.Panel();
			this.loadDataPanel = new System.Windows.Forms.Panel();
			this.filenameTextBox = new System.Windows.Forms.TextBox();
			this.label1 = new System.Windows.Forms.Label();
			this.backgroundWorker1 = new System.ComponentModel.BackgroundWorker();
			this.stackPanel1 = new Final_App.StackPanel();
			this.emptyTab = new System.Windows.Forms.TabPage();
			this.loadDataTab = new System.Windows.Forms.TabPage();
			this.dataInfoTab = new System.Windows.Forms.TabPage();
			this.dataInfoPanel = new System.Windows.Forms.Panel();
			this.label2 = new System.Windows.Forms.Label();
			this.dataInfoLabel = new System.Windows.Forms.Label();
			this.catToNumTab = new System.Windows.Forms.TabPage();
			this.catToNumPanel = new System.Windows.Forms.Panel();
			this.label3 = new System.Windows.Forms.Label();
			this.label4 = new System.Windows.Forms.Label();
			this.label5 = new System.Windows.Forms.Label();
			this.radioButtonPanel = new System.Windows.Forms.Panel();
			this.labelEncodingRadio = new System.Windows.Forms.RadioButton();
			this.oneHotRadio = new System.Windows.Forms.RadioButton();
			this.missingValueTab = new System.Windows.Forms.TabPage();
			this.missingValuePanel = new System.Windows.Forms.Panel();
			this.tableLayoutPanel1.SuspendLayout();
			this.flowLayoutPanel1.SuspendLayout();
			this.groupBox2.SuspendLayout();
			this.groupBox1.SuspendLayout();
			this.flowLayoutPanel2.SuspendLayout();
			this.loadDataPanel.SuspendLayout();
			this.stackPanel1.SuspendLayout();
			this.emptyTab.SuspendLayout();
			this.loadDataTab.SuspendLayout();
			this.dataInfoTab.SuspendLayout();
			this.dataInfoPanel.SuspendLayout();
			this.catToNumTab.SuspendLayout();
			this.catToNumPanel.SuspendLayout();
			this.radioButtonPanel.SuspendLayout();
			this.missingValueTab.SuspendLayout();
			this.SuspendLayout();
			// 
			// tableLayoutPanel1
			// 
			this.tableLayoutPanel1.CellBorderStyle = System.Windows.Forms.TableLayoutPanelCellBorderStyle.Single;
			this.tableLayoutPanel1.ColumnCount = 2;
			this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 30F));
			this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 70F));
			this.tableLayoutPanel1.Controls.Add(this.flowLayoutPanel1, 1, 0);
			this.tableLayoutPanel1.Controls.Add(this.flowLayoutPanel2, 1, 2);
			this.tableLayoutPanel1.Controls.Add(this.stackPanel1, 1, 1);
			this.tableLayoutPanel1.Dock = System.Windows.Forms.DockStyle.Fill;
			this.tableLayoutPanel1.Location = new System.Drawing.Point(0, 0);
			this.tableLayoutPanel1.Name = "tableLayoutPanel1";
			this.tableLayoutPanel1.RowCount = 3;
			this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 13F));
			this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 82F));
			this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 5F));
			this.tableLayoutPanel1.Size = new System.Drawing.Size(1361, 808);
			this.tableLayoutPanel1.TabIndex = 0;
			// 
			// flowLayoutPanel1
			// 
			this.flowLayoutPanel1.BackColor = System.Drawing.SystemColors.Control;
			this.flowLayoutPanel1.Controls.Add(this.groupBox2);
			this.flowLayoutPanel1.Controls.Add(this.groupBox1);
			this.flowLayoutPanel1.Dock = System.Windows.Forms.DockStyle.Fill;
			this.flowLayoutPanel1.Location = new System.Drawing.Point(412, 4);
			this.flowLayoutPanel1.Name = "flowLayoutPanel1";
			this.flowLayoutPanel1.Size = new System.Drawing.Size(945, 98);
			this.flowLayoutPanel1.TabIndex = 2;
			// 
			// groupBox2
			// 
			this.groupBox2.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left)));
			this.groupBox2.AutoSize = true;
			this.groupBox2.Controls.Add(this.dataInputDropDown);
			this.groupBox2.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
			this.groupBox2.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.groupBox2.Location = new System.Drawing.Point(3, 3);
			this.groupBox2.Name = "groupBox2";
			this.groupBox2.Size = new System.Drawing.Size(200, 91);
			this.groupBox2.TabIndex = 1;
			this.groupBox2.TabStop = false;
			this.groupBox2.Text = "Data Input";
			// 
			// dataInputDropDown
			// 
			this.dataInputDropDown.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left)));
			this.dataInputDropDown.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.dataInputDropDown.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
			this.dataInputDropDown.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.dataInputDropDown.FormattingEnabled = true;
			this.dataInputDropDown.Items.AddRange(new object[] {
            "Load Data",
            "Data Info."});
			this.dataInputDropDown.Location = new System.Drawing.Point(6, 38);
			this.dataInputDropDown.Name = "dataInputDropDown";
			this.dataInputDropDown.Size = new System.Drawing.Size(188, 28);
			this.dataInputDropDown.TabIndex = 0;
			this.dataInputDropDown.SelectedIndexChanged += new System.EventHandler(this.dataInputDropDown_SelectedIndexChanged);
			// 
			// groupBox1
			// 
			this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left)));
			this.groupBox1.AutoSize = true;
			this.groupBox1.Controls.Add(this.preProcessDropDown);
			this.groupBox1.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
			this.groupBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.groupBox1.Location = new System.Drawing.Point(209, 3);
			this.groupBox1.Name = "groupBox1";
			this.groupBox1.Size = new System.Drawing.Size(329, 91);
			this.groupBox1.TabIndex = 0;
			this.groupBox1.TabStop = false;
			this.groupBox1.Text = "Data Pre-processing";
			// 
			// preProcessDropDown
			// 
			this.preProcessDropDown.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.preProcessDropDown.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
			this.preProcessDropDown.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.preProcessDropDown.FormattingEnabled = true;
			this.preProcessDropDown.Items.AddRange(new object[] {
            "Categorical to Numerical Conversion",
            "Missing Value Handling",
            "Scaling"});
			this.preProcessDropDown.Location = new System.Drawing.Point(6, 38);
			this.preProcessDropDown.Name = "preProcessDropDown";
			this.preProcessDropDown.Size = new System.Drawing.Size(317, 28);
			this.preProcessDropDown.TabIndex = 0;
			this.preProcessDropDown.SelectedIndexChanged += new System.EventHandler(this.preProcessDropDown_SelectedIndexChanged);
			// 
			// flowLayoutPanel2
			// 
			this.flowLayoutPanel2.Controls.Add(this.submitButton);
			this.flowLayoutPanel2.Dock = System.Windows.Forms.DockStyle.Fill;
			this.flowLayoutPanel2.FlowDirection = System.Windows.Forms.FlowDirection.RightToLeft;
			this.flowLayoutPanel2.Location = new System.Drawing.Point(412, 769);
			this.flowLayoutPanel2.Name = "flowLayoutPanel2";
			this.flowLayoutPanel2.Size = new System.Drawing.Size(945, 35);
			this.flowLayoutPanel2.TabIndex = 5;
			// 
			// submitButton
			// 
			this.submitButton.AutoSize = true;
			this.submitButton.Dock = System.Windows.Forms.DockStyle.Right;
			this.submitButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.submitButton.Location = new System.Drawing.Point(867, 3);
			this.submitButton.Name = "submitButton";
			this.submitButton.Size = new System.Drawing.Size(75, 30);
			this.submitButton.TabIndex = 4;
			this.submitButton.Text = "Submit";
			this.submitButton.UseVisualStyleBackColor = true;
			this.submitButton.Click += new System.EventHandler(this.submitButton_Click);
			// 
			// emptyPanel
			// 
			this.emptyPanel.BackColor = System.Drawing.SystemColors.Control;
			this.emptyPanel.Dock = System.Windows.Forms.DockStyle.Fill;
			this.emptyPanel.Location = new System.Drawing.Point(3, 3);
			this.emptyPanel.Name = "emptyPanel";
			this.emptyPanel.Size = new System.Drawing.Size(931, 618);
			this.emptyPanel.TabIndex = 6;
			// 
			// loadDataPanel
			// 
			this.loadDataPanel.AutoScroll = true;
			this.loadDataPanel.BackColor = System.Drawing.SystemColors.Control;
			this.loadDataPanel.Controls.Add(this.label3);
			this.loadDataPanel.Controls.Add(this.filenameTextBox);
			this.loadDataPanel.Controls.Add(this.label1);
			this.loadDataPanel.Dock = System.Windows.Forms.DockStyle.Fill;
			this.loadDataPanel.Location = new System.Drawing.Point(3, 3);
			this.loadDataPanel.Name = "loadDataPanel";
			this.loadDataPanel.Size = new System.Drawing.Size(931, 618);
			this.loadDataPanel.TabIndex = 3;
			// 
			// filenameTextBox
			// 
			this.filenameTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.filenameTextBox.Location = new System.Drawing.Point(470, 330);
			this.filenameTextBox.Name = "filenameTextBox";
			this.filenameTextBox.Size = new System.Drawing.Size(297, 36);
			this.filenameTextBox.TabIndex = 1;
			// 
			// label1
			// 
			this.label1.AutoSize = true;
			this.label1.Font = new System.Drawing.Font("Lucida Sans", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label1.Location = new System.Drawing.Point(4, 330);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(433, 29);
			this.label1.TabIndex = 0;
			this.label1.Text = "Enter the filename of the dataset:";
			// 
			// backgroundWorker1
			// 
			this.backgroundWorker1.DoWork += new System.ComponentModel.DoWorkEventHandler(this.backgroundWorker1_DoWork);
			this.backgroundWorker1.RunWorkerCompleted += new System.ComponentModel.RunWorkerCompletedEventHandler(this.backgroundWorker1_RunWorkerCompleted);
			// 
			// stackPanel1
			// 
			this.stackPanel1.Controls.Add(this.emptyTab);
			this.stackPanel1.Controls.Add(this.loadDataTab);
			this.stackPanel1.Controls.Add(this.dataInfoTab);
			this.stackPanel1.Controls.Add(this.catToNumTab);
			this.stackPanel1.Controls.Add(this.missingValueTab);
			this.stackPanel1.Dock = System.Windows.Forms.DockStyle.Fill;
			this.stackPanel1.Location = new System.Drawing.Point(412, 109);
			this.stackPanel1.Name = "stackPanel1";
			this.stackPanel1.SelectedIndex = 0;
			this.stackPanel1.Size = new System.Drawing.Size(945, 653);
			this.stackPanel1.TabIndex = 7;
			// 
			// emptyTab
			// 
			this.emptyTab.Controls.Add(this.emptyPanel);
			this.emptyTab.Location = new System.Drawing.Point(4, 25);
			this.emptyTab.Name = "emptyTab";
			this.emptyTab.Padding = new System.Windows.Forms.Padding(3);
			this.emptyTab.Size = new System.Drawing.Size(937, 624);
			this.emptyTab.TabIndex = 0;
			this.emptyTab.Text = "Empty";
			this.emptyTab.UseVisualStyleBackColor = true;
			// 
			// loadDataTab
			// 
			this.loadDataTab.Controls.Add(this.loadDataPanel);
			this.loadDataTab.Location = new System.Drawing.Point(4, 25);
			this.loadDataTab.Name = "loadDataTab";
			this.loadDataTab.Padding = new System.Windows.Forms.Padding(3);
			this.loadDataTab.Size = new System.Drawing.Size(937, 624);
			this.loadDataTab.TabIndex = 1;
			this.loadDataTab.Text = "Load Data";
			this.loadDataTab.UseVisualStyleBackColor = true;
			// 
			// dataInfoTab
			// 
			this.dataInfoTab.Controls.Add(this.dataInfoPanel);
			this.dataInfoTab.Location = new System.Drawing.Point(4, 25);
			this.dataInfoTab.Name = "dataInfoTab";
			this.dataInfoTab.Size = new System.Drawing.Size(937, 624);
			this.dataInfoTab.TabIndex = 2;
			this.dataInfoTab.Text = "Data Info";
			this.dataInfoTab.UseVisualStyleBackColor = true;
			// 
			// dataInfoPanel
			// 
			this.dataInfoPanel.AutoScroll = true;
			this.dataInfoPanel.Controls.Add(this.dataInfoLabel);
			this.dataInfoPanel.Controls.Add(this.label2);
			this.dataInfoPanel.Dock = System.Windows.Forms.DockStyle.Fill;
			this.dataInfoPanel.Location = new System.Drawing.Point(0, 0);
			this.dataInfoPanel.Name = "dataInfoPanel";
			this.dataInfoPanel.Size = new System.Drawing.Size(937, 624);
			this.dataInfoPanel.TabIndex = 0;
			// 
			// label2
			// 
			this.label2.AutoSize = true;
			this.label2.Font = new System.Drawing.Font("Lucida Sans", 20F, System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label2.Location = new System.Drawing.Point(3, 26);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(178, 39);
			this.label2.TabIndex = 0;
			this.label2.Text = "Data Info.";
			// 
			// dataInfoLabel
			// 
			this.dataInfoLabel.AutoSize = true;
			this.dataInfoLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 13F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.dataInfoLabel.Location = new System.Drawing.Point(5, 95);
			this.dataInfoLabel.Name = "dataInfoLabel";
			this.dataInfoLabel.Size = new System.Drawing.Size(70, 26);
			this.dataInfoLabel.TabIndex = 1;
			this.dataInfoLabel.Text = "label3";
			// 
			// catToNumTab
			// 
			this.catToNumTab.Controls.Add(this.catToNumPanel);
			this.catToNumTab.Location = new System.Drawing.Point(4, 25);
			this.catToNumTab.Name = "catToNumTab";
			this.catToNumTab.Size = new System.Drawing.Size(937, 624);
			this.catToNumTab.TabIndex = 3;
			this.catToNumTab.Text = "Cat To Num";
			this.catToNumTab.UseVisualStyleBackColor = true;
			// 
			// catToNumPanel
			// 
			this.catToNumPanel.Controls.Add(this.radioButtonPanel);
			this.catToNumPanel.Controls.Add(this.label5);
			this.catToNumPanel.Controls.Add(this.label4);
			this.catToNumPanel.Dock = System.Windows.Forms.DockStyle.Fill;
			this.catToNumPanel.Location = new System.Drawing.Point(0, 0);
			this.catToNumPanel.Name = "catToNumPanel";
			this.catToNumPanel.Size = new System.Drawing.Size(937, 624);
			this.catToNumPanel.TabIndex = 0;
			// 
			// label3
			// 
			this.label3.AutoSize = true;
			this.label3.Font = new System.Drawing.Font("Lucida Sans", 20F, System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label3.Location = new System.Drawing.Point(6, 40);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(234, 39);
			this.label3.TabIndex = 2;
			this.label3.Text = "Data Loading";
			// 
			// label4
			// 
			this.label4.AutoSize = true;
			this.label4.Font = new System.Drawing.Font("Lucida Sans", 20F, System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label4.Location = new System.Drawing.Point(15, 44);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(500, 39);
			this.label4.TabIndex = 3;
			this.label4.Text = "Categorical Feature Handling";
			// 
			// label5
			// 
			this.label5.AutoSize = true;
			this.label5.Font = new System.Drawing.Font("Lucida Sans", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label5.Location = new System.Drawing.Point(17, 200);
			this.label5.Name = "label5";
			this.label5.Size = new System.Drawing.Size(359, 29);
			this.label5.TabIndex = 4;
			this.label5.Text = "Select the type of encoding:";
			// 
			// radioButtonPanel
			// 
			this.radioButtonPanel.AutoSize = true;
			this.radioButtonPanel.Controls.Add(this.oneHotRadio);
			this.radioButtonPanel.Controls.Add(this.labelEncodingRadio);
			this.radioButtonPanel.Location = new System.Drawing.Point(22, 277);
			this.radioButtonPanel.Name = "radioButtonPanel";
			this.radioButtonPanel.Size = new System.Drawing.Size(207, 100);
			this.radioButtonPanel.TabIndex = 5;
			// 
			// labelEncodingRadio
			// 
			this.labelEncodingRadio.AutoSize = true;
			this.labelEncodingRadio.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.labelEncodingRadio.Location = new System.Drawing.Point(12, 15);
			this.labelEncodingRadio.Name = "labelEncodingRadio";
			this.labelEncodingRadio.Size = new System.Drawing.Size(168, 29);
			this.labelEncodingRadio.TabIndex = 0;
			this.labelEncodingRadio.TabStop = true;
			this.labelEncodingRadio.Text = "Label Encoding";
			this.labelEncodingRadio.UseVisualStyleBackColor = true;
			// 
			// oneHotRadio
			// 
			this.oneHotRadio.AutoSize = true;
			this.oneHotRadio.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.oneHotRadio.Location = new System.Drawing.Point(12, 60);
			this.oneHotRadio.Name = "oneHotRadio";
			this.oneHotRadio.Size = new System.Drawing.Size(192, 29);
			this.oneHotRadio.TabIndex = 1;
			this.oneHotRadio.TabStop = true;
			this.oneHotRadio.Text = "One-hot Encoding";
			this.oneHotRadio.UseVisualStyleBackColor = true;
			// 
			// missingValueTab
			// 
			this.missingValueTab.Controls.Add(this.missingValuePanel);
			this.missingValueTab.Location = new System.Drawing.Point(4, 25);
			this.missingValueTab.Name = "missingValueTab";
			this.missingValueTab.Size = new System.Drawing.Size(937, 624);
			this.missingValueTab.TabIndex = 4;
			this.missingValueTab.Text = "Missing values";
			this.missingValueTab.UseVisualStyleBackColor = true;
			// 
			// missingValuePanel
			// 
			this.missingValuePanel.Dock = System.Windows.Forms.DockStyle.Fill;
			this.missingValuePanel.Location = new System.Drawing.Point(0, 0);
			this.missingValuePanel.Name = "missingValuePanel";
			this.missingValuePanel.Size = new System.Drawing.Size(937, 624);
			this.missingValuePanel.TabIndex = 0;
			// 
			// Final_Application
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.AutoScroll = true;
			this.AutoSize = true;
			this.ClientSize = new System.Drawing.Size(1361, 808);
			this.Controls.Add(this.tableLayoutPanel1);
			this.Name = "Final_Application";
			this.Text = "Final Application";
			this.WindowState = System.Windows.Forms.FormWindowState.Maximized;
			this.Load += new System.EventHandler(this.Final_Application_Load);
			this.tableLayoutPanel1.ResumeLayout(false);
			this.flowLayoutPanel1.ResumeLayout(false);
			this.flowLayoutPanel1.PerformLayout();
			this.groupBox2.ResumeLayout(false);
			this.groupBox1.ResumeLayout(false);
			this.flowLayoutPanel2.ResumeLayout(false);
			this.flowLayoutPanel2.PerformLayout();
			this.loadDataPanel.ResumeLayout(false);
			this.loadDataPanel.PerformLayout();
			this.stackPanel1.ResumeLayout(false);
			this.emptyTab.ResumeLayout(false);
			this.loadDataTab.ResumeLayout(false);
			this.dataInfoTab.ResumeLayout(false);
			this.dataInfoPanel.ResumeLayout(false);
			this.dataInfoPanel.PerformLayout();
			this.catToNumTab.ResumeLayout(false);
			this.catToNumPanel.ResumeLayout(false);
			this.catToNumPanel.PerformLayout();
			this.radioButtonPanel.ResumeLayout(false);
			this.radioButtonPanel.PerformLayout();
			this.missingValueTab.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
		private System.Windows.Forms.GroupBox groupBox1;
		private System.Windows.Forms.ComboBox preProcessDropDown;
		private System.Windows.Forms.GroupBox groupBox2;
		private System.Windows.Forms.ComboBox dataInputDropDown;
		private System.Windows.Forms.FlowLayoutPanel flowLayoutPanel1;
		private System.Windows.Forms.Panel loadDataPanel;
		private System.Windows.Forms.TextBox filenameTextBox;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.FlowLayoutPanel flowLayoutPanel2;
		private System.Windows.Forms.Button submitButton;
		private System.Windows.Forms.Panel emptyPanel;
		private System.ComponentModel.BackgroundWorker backgroundWorker1;
		private StackPanel stackPanel1;
		private System.Windows.Forms.TabPage emptyTab;
		private System.Windows.Forms.TabPage loadDataTab;
		private System.Windows.Forms.TabPage dataInfoTab;
		private System.Windows.Forms.Panel dataInfoPanel;
		private System.Windows.Forms.Label dataInfoLabel;
		private System.Windows.Forms.Label label2;
		private System.Windows.Forms.TabPage catToNumTab;
		private System.Windows.Forms.Panel catToNumPanel;
		private System.Windows.Forms.Label label3;
		private System.Windows.Forms.Label label5;
		private System.Windows.Forms.Label label4;
		private System.Windows.Forms.Panel radioButtonPanel;
		private System.Windows.Forms.RadioButton oneHotRadio;
		private System.Windows.Forms.RadioButton labelEncodingRadio;
		private System.Windows.Forms.TabPage missingValueTab;
		private System.Windows.Forms.Panel missingValuePanel;
	}
}

