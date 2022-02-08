# Audio Steganography using RSA and ChaCha-20 Encryption Techniques

The proposed algorithm introduces a multilevel approach to the existing LSB encoding technique.

The proposed algorithm is designed to use stereo audio with WAV format sampled at any frequency. Using two different cryptography methods (one symmetric key and one public-key cryptography), the algorithm can enhance the security of the embedded data in the audio file.

The embedding algorithm is divided into four steps, and it takes place at the sender’s end. Below image shows all the steps involved in the embedding process. The presented technique utilizes ChaCha20 and RSA encryption algorithms to attain - (i) decent hiding quantity & (ii) improved security using a public key cryptosystem and a modified version of Least Significant Bit (LSB) encoding technique to embed the encrypted data in the cover audio file

<img src="https://user-images.githubusercontent.com/59963061/125196923-45820080-e279-11eb-9052-2c69e038925e.png" width="90%"></img>

The main purpose of the proposed method is to make gaining unauthorized access to confidential data increasingly difficult. For this reason, cryptography has been used in conjunction with steganography to provide enhanced data protection. The media hidden as the secret message inside the cover audio file does not affect the size of the cover audio file, thus making detection of hidden data inside the carrier audio file, difficult for an unauthorized third party.

The parameters used for evaluating the efficacy of the proposed technique were SNR, PSNR, RMSE, and MAE. High values of SNR and PSNR and low values of RMSE and MAE were observed for both the text as well as the image used as a secret message hidden in a cover audio file.

These values indicate that there is a minimal difference between the original audio file and the stego audio file and thus there is a very low perceptual distortion in the stego audio file. This ensures imperceptibility, which makes it difficult to detect the secret message concealed inside the cover audio file.
