namespace WindowsFormsApp1
{
	partial class FibonacciCalculator
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
			this.numericUpDown1 = new System.Windows.Forms.NumericUpDown();
			this.startAsyncButton = new System.Windows.Forms.Button();
			this.cancelAsyncButton = new System.Windows.Forms.Button();
			this.resultLabel = new System.Windows.Forms.Label();
			this.progressBar1 = new System.Windows.Forms.ProgressBar();
			this.backgroundWorker1 = new System.ComponentModel.BackgroundWorker();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).BeginInit();
			this.SuspendLayout();
			// 
			// numericUpDown1
			// 
			this.numericUpDown1.Location = new System.Drawing.Point(12, 51);
			this.numericUpDown1.Maximum = new decimal(new int[] {
            91,
            0,
            0,
            0});
			this.numericUpDown1.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericUpDown1.Name = "numericUpDown1";
			this.numericUpDown1.Size = new System.Drawing.Size(120, 22);
			this.numericUpDown1.TabIndex = 0;
			this.numericUpDown1.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			// 
			// startAsyncButton
			// 
			this.startAsyncButton.AutoSize = true;
			this.startAsyncButton.Location = new System.Drawing.Point(408, 313);
			this.startAsyncButton.Name = "startAsyncButton";
			this.startAsyncButton.Size = new System.Drawing.Size(90, 27);
			this.startAsyncButton.TabIndex = 1;
			this.startAsyncButton.Text = "Start Async";
			this.startAsyncButton.UseVisualStyleBackColor = true;
			this.startAsyncButton.Click += new System.EventHandler(this.startAsyncButton_Click);
			// 
			// cancelAsyncButton
			// 
			this.cancelAsyncButton.AutoSize = true;
			this.cancelAsyncButton.Enabled = false;
			this.cancelAsyncButton.Location = new System.Drawing.Point(546, 313);
			this.cancelAsyncButton.Name = "cancelAsyncButton";
			this.cancelAsyncButton.Size = new System.Drawing.Size(103, 27);
			this.cancelAsyncButton.TabIndex = 2;
			this.cancelAsyncButton.Text = "Cancel Async";
			this.cancelAsyncButton.UseVisualStyleBackColor = true;
			this.cancelAsyncButton.Click += new System.EventHandler(this.cancelAsyncButton_Click);
			// 
			// resultLabel
			// 
			this.resultLabel.AutoSize = true;
			this.resultLabel.Location = new System.Drawing.Point(22, 161);
			this.resultLabel.Name = "resultLabel";
			this.resultLabel.Size = new System.Drawing.Size(46, 17);
			this.resultLabel.TabIndex = 3;
			this.resultLabel.Text = "label1";
			// 
			// progressBar1
			// 
			this.progressBar1.Location = new System.Drawing.Point(339, 13);
			this.progressBar1.Name = "progressBar1";
			this.progressBar1.Size = new System.Drawing.Size(100, 23);
			this.progressBar1.TabIndex = 4;
			// 
			// backgroundWorker1
			// 
			this.backgroundWorker1.WorkerReportsProgress = true;
			this.backgroundWorker1.WorkerSupportsCancellation = true;
			this.backgroundWorker1.DoWork += new System.ComponentModel.DoWorkEventHandler(this.backgroundWorker1_DoWork);
			this.backgroundWorker1.ProgressChanged += new System.ComponentModel.ProgressChangedEventHandler(this.backgroundWorker1_ProgressChanged);
			this.backgroundWorker1.RunWorkerCompleted += new System.ComponentModel.RunWorkerCompletedEventHandler(this.backgroundWorker1_RunWorkerCompleted);
			// 
			// FibonacciCalculator
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(800, 450);
			this.Controls.Add(this.progressBar1);
			this.Controls.Add(this.resultLabel);
			this.Controls.Add(this.cancelAsyncButton);
			this.Controls.Add(this.startAsyncButton);
			this.Controls.Add(this.numericUpDown1);
			this.Name = "FibonacciCalculator";
			this.Text = "Form1";
			((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.NumericUpDown numericUpDown1;
		private System.Windows.Forms.Button startAsyncButton;
		private System.Windows.Forms.Button cancelAsyncButton;
		private System.Windows.Forms.Label resultLabel;
		private System.Windows.Forms.ProgressBar progressBar1;
		private System.ComponentModel.BackgroundWorker backgroundWorker1;
	}
}

