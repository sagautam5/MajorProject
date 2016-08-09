struct header_key
    {
        int sizeof_hdr;
        char data_type[10];
        char db_name[18];
        int extents;
        short int session_error;
        char regular;
        char hkey_un0;
    };
    
struct image_dimension
    {
        short int dim[8];
        short int unused8;
        short int unused9;
        short int unused10;
        short int unused11;
        short int unused12;
        short int unused13;
        short int unused14;
        short int datatype;
        short int bitpix;
        short int dim_un0;
   	
	char vox_units[4];
	char cal_units[4];

        float pixdim[8];
        float vox_offset;
        float funused1;
        float funused2;
        float funused3;
        float cal_max;
        float cal_min;
        float compressed;
        float verified;
        int glmax,glmin;
    };

struct data_history
    {
        char descrip[80];
        char aux_file[24];
        char orient;
        char originator[10];
        char generated[10];
        char scannum[10];
        char patient_id[10];
        char exp_date[10];
        char exp_time[10];
        char hist_un0[3];
        
        int views;
        int vols_added;
        int start_field;
        int field_skip;
        int omax,omin;
        int smax,smin;
    };

struct dsr
    {
    
        struct header_key hk;
        struct image_dimension dime;
        struct data_history hist;
    };
#define DT_NONE              0
#define DT_UNKNOWN           0
#define DT_BINERY            1
#define DT_UNSIGNED_CHAR     2
#define DT_SIGNED_SHORT      4
#define DT_SIGNED_INT        8
#define DT_FLOAT             16
#define DT_COMPLEX           32
#define DT_DOUBLE            64
#define DT_RGB               128
#define DT_ALL               255

typedef struct
    {
    float real;
    float imag;
    }COMPLEX;
