package net.premierphotobooth.cfausn.premierphotoscanner;
import android.content.DialogInterface;
import android.content.pm.ActivityInfo;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.os.StrictMode;
import android.provider.MediaStore;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;

import com.google.zxing.Result;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;

import me.dm7.barcodescanner.core.BarcodeScannerView;
import me.dm7.barcodescanner.zxing.ZXingScannerView;

public class MainActivity extends AppCompatActivity implements ZXingScannerView.ResultHandler {
    private ZXingScannerView mScannerView;

    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);

    }

    public void QrScanner(View view){

        mScannerView = new ZXingScannerView(this);   // Programmatically initialize the scanner view
        setContentView(mScannerView);
        mScannerView.setResultHandler(this); // Register ourselves as a handler for scan results.
        mScannerView.startCamera();         // Start camera
    }

    @Override
    public void onPause() {
        super.onPause();
        mScannerView.stopCamera();   // Stop camera on pause
    }

    @Override
    public void handleResult(final Result rawResult) {
        // Do something with the result here

        Log.e("handler", rawResult.getText()); // Prints scan results
        Log.e("handler", rawResult.getBarcodeFormat().toString()); // Prints the scan format (qrcode)

        final ImageView imageView = new ImageView(getApplicationContext());
        final Bitmap[] image = new Bitmap[1];





        new Thread() {

            public void run() {

                try {

                    String[] qrVals = rawResult.getText().split(",");
                    StringBuilder url = new StringBuilder();

                    url.append("http://www.premierphotobooth.net/CSVs/");
                    url.append(qrVals[2]);
                    url.append(qrVals[1]);
                    url.append(".csv");

                    String theURL = url.toString();

                    BufferedReader in = new BufferedReader(
                            new InputStreamReader(
                                    new URL(theURL).openStream()));

                    String inputLine;
                    String albumName;
                    StringBuilder builder = new StringBuilder();

                    while ((inputLine = in.readLine()) != null) {
                        String[] csvVals = inputLine.split(",");

                        if(csvVals.length > 2){
                            builder.append("http://www.premierphotobooth.net/photos/");
                            for(int i = 0; i < csvVals.length; i++){
                                builder.append(csvVals[i]);
                            }
                            builder.append("-");
                            //albumName = builder.toString();
                        }
                        else if(csvVals[0].equals(qrVals[0])){
                            String[] dateVals = qrVals[1].split("-");
                            builder.append(dateVals[1].replaceFirst("^0*",""));
                            builder.append("/");
                            builder.append(dateVals[2].replaceFirst("^0*",""));
                            builder.append("/");
                            builder.append(dateVals[0]);
                            builder.append("/");
                            builder.append(csvVals[1]);
                            albumName = builder.toString();
                            break;

                        }
                        //System.out.println(inputLine);
                    }
                    in.close();
                    Log.e("URL", builder.toString()); // Prints scan results


                    image[0] = BitmapFactory.decodeStream(new URL(builder.toString()).openStream());
                } catch (IOException e) {
                    e.printStackTrace();
                }
                runOnUiThread(new Runnable() {

                    @Override
                    public void run() {

                        imageView.setImageBitmap(image[0]);
                    }
                });
            }
        }.start();

        final MainActivity bs = this;
        AlertDialog dialog = new AlertDialog.Builder(this)
                .setView(imageView)
                .setTitle("Loading... please wait")
                .setPositiveButton("save", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        MediaStore.Images.Media.insertImage(getContentResolver(), image[0], rawResult.getText(), "Your premier photoboth photo");
                        dialog.dismiss();
                        mScannerView.resumeCameraPreview(bs);

                    }
                })
                .setNegativeButton("cancel", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        dialog.dismiss();
                        mScannerView.resumeCameraPreview(bs);
                    }
                }).create();
        dialog.show();

        // show the scanner result into dialog box.
        /*
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("Scan Result");
        builder.setMessage(rawResult.getText());
        AlertDialog alert1 = builder.create();
        alert1.show();*/

        // If you would like to resume scanning, call this method below:

        //if(resumeCamera[0]) mScannerView.resumeCameraPreview(this);
    }


}
